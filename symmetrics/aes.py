import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random key for AES
key = b'this is a secret' #get_random_bytes(16)
key64 = base64.b64encode(key).decode('utf-8')

# Encrypt some data
data = b"Secret Message"
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
ciphertext64 = base64.b64encode(ciphertext).decode('utf-8')

# Store nonce and ciphertext
nonce = cipher.nonce
nonce64 = base64.b64encode(nonce).decode('utf-8')

# Decrypt the data
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)

print(f"Ciphertext: {ciphertext64}")
print(f"Key: {key64}")
print(f"Nonce: {nonce64}")
print(f"Decrypted: {plaintext}")
