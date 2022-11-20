// SPDX-License-Identifier: MIT
pragma solidity 0.8.17;

contract SNDB {
    // Maps socialAccount -> assetName -> CID.
    // ex: twitter:@tier10k -> profile.json -> CID
    // ex: twitter:@tier10k -> avatar.png -> CID
    mapping(string => mapping(string => string)) userAssets;

    // Approved on-chain addresses for social accounts.
    mapping(string => address) approvals;

    // Token balances.
    mapping(address => uint) balances;

    address owner;

    constructor() {
        owner = tx.origin;
        balances[tx.origin] = 1000000000;
    }

    function sendCoin(
        address receiver,
        uint amount
    ) public returns (bool sufficient) {
        if (balances[msg.sender] < amount) return false;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        return true;
    }

    function getBalance(address addr) public view returns (uint) {
        return balances[addr];
    }

    // Private method to mint tokens for uploading assets
    function mintTo(address receiver, uint amount) private {
        balances[receiver] += amount;
    }

    // Enables <address> to upload data for specific social network. Centralized for now.
    function approveForAccount(address addr, string calldata socialAccount) public {
        require(msg.sender == owner);
        approvals[socialAccount] = addr;
        mintTo(addr, 1000); // mint a few tokens for registering address
    }

    // Registers social network assets.
    function addAsset(string calldata socialAccount, string calldata assetName, string calldata CID) public {
        require(msg.sender == approvals[socialAccount]);
        userAssets[socialAccount][assetName] = CID;
        mintTo(msg.sender, 10000); // mint tokens for adding data
    }
}
