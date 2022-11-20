# Getting Started

- Python script will do the following:
  - Auth to Twitter
  - Download social data using auth token
  - Upload assets to IPFS and save CID's
  - Invoke Filecoin FEVM smart contract to register assets

# Contract Details

Contract was deployed in this transaction:
https://explorer.glif.io/wallaby/tx/0x68def3f0a4201dd9e298eea874719f16e6486e3b3ab1c4ed50636e8b33f68f70/

Address:
0x5219bDD63e447c3E00dA9867CFAfC0Eb7041d259

# Example Contract Invocations

Approve address to post for "twitter:tier10k" (only owner can do this -- will be done by web service in future):
https://explorer.glif.io/wallaby/tx/0x61e6ac68d2df706c23424215e935c6e9de36f151d185cd5b05fd0af6cab415ff/

Try to set assets for "twitter:asdf" but fail since there are no approvals:
https://explorer.glif.io/wallaby/tx/0x272cf2b7465a391bc3d3f4b73abea955ab154609dfd1cef582fee44124c8a5e7/

Set "avatar.jpg" for "twitter:tier10k" successfully:
https://explorer.glif.io/wallaby/tx/0x060e3f8078cb62bdffbefc6fcd774bad2c03de2bc9a261d7a47f2732a3084c53/

Balance of user as retrieved from getBalance() is now +11000.
