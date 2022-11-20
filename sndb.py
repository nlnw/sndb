#%% First retrieve the user's avatar.
print("Getting twitter avatar...")
from requests_oauthlib import OAuth1Session
import os
import json

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = "AgU08rZn2KDuFfxDDEI9Ns7"
consumer_secret = "0V3YIoWPHdHPSIg2knsHdhJlSxFC4F4UR7fThvY1hvNBIJeD"

# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld
fields = "created_at,description,profile_image_url"
params = {"usernames": "TwitterDev,TwitterAPI", "user.fields": fields}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError as e:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered.",
        e,
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.get("https://api.twitter.com/2/users/by", params=params)

if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()

print(json.dumps(json_response, indent=4, sort_keys=True))

profile_image_url = json_response["profile_image_url"]

#%% Then, upload it to IPFS
print("Uploading to IPFS...")
import ipfshttpclient

client = ipfshttpclient.connect(os.getenv["IPFS_CONNECT_URL"])
res = client.add(profile_image_url)
CID = res["hash"]

#%% Then, register it to the FEVM contract
print("Writing to FEVM contract...")
from web3 import Web3

# wallaby testnet
w3 = Web3(Web3.HTTPProvider("https://wallaby.node.glif.io/rpc/v0"))

# chainid: 31415

CONTRACT_ADDRESS = "0x5219bDD63e447c3E00dA9867CFAfC0Eb7041d259"
ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "socialAccount", "type": "string"},
            {"internalType": "string", "name": "assetName", "type": "string"},
            {"internalType": "string", "name": "CID", "type": "string"},
        ],
        "name": "addAsset",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "addr", "type": "address"},
            {"internalType": "string", "name": "socialAccount", "type": "string"},
        ],
        "name": "approveForAccount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "receiver", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "sendCoin",
        "outputs": [{"internalType": "bool", "name": "sufficient", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "inputs": [{"internalType": "address", "name": "addr", "type": "address"}],
        "name": "getBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

sndb_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
sndb_contract.functions.addAsset(
    "twitter:tier10k",
    "avatar.jpg",
    "bafybeibhrr2cmsra6wbki3hvopdqo2nx33qavssgwcekvtsqyoxdohpdj4",
)

print("Done!")
