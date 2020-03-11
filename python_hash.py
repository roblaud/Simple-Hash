import hmac
import hashlib

message = 'Hello, this is a test'
print('Your original message was: ' + '\'' + message + '\'')

# This can be changed to any algorithom supported by hashlib
hash_alg = hashlib.sha256

# Encodes the message so that it can be properly hashed
encoded_message = message.encode('utf-8')
# Key must be given in bytes, digest is the hash algorithom for use
message_hash = hmac.digest(bytes(128), msg=encoded_message, digest=hash_alg)
print('Your message after using the SHA256 algorithom was: ' + str(message_hash))

# DEBUG: Prints available hashing algorithoms
# print(hashlib.algorithms_available)
