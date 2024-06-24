pragma solidity ^0.8.0;

contract ContentVerifier {
    mapping (address => mapping (string => bool)) public contentVerification;

    event ContentVerified(address indexed user, string contentId, bool isValid);

    function verifyContent(address user, string memory contentId, bytes memory contentHash) public {
        require(msg.sender == user, "Only the content owner can verify content");
        bytes32 contentHashBytes = keccak256(contentHash);
        if (contentVerification[user][contentId] == false) {
            contentVerification[user][contentId] = true;
            emit ContentVerified(user, contentId, true);
        }
    }

    function getContentVerification(address user, string memory contentId) public view returns (bool) {
        return contentVerification[user][contentId];
    }
}
