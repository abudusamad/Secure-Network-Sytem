from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
private_key, public_key = key, key.publickey()


plain_text="this is the message"
cipher = PKCS1_OAEP.new(public_key)
encrypted_text=cipher.encrypt(plain_text.encode("utf8"))
encrypted_text64 = base64.b64encode(encrypted_text).decode('utf-8')

print(f"\n\nprivate key:\n{private_key.export_key(format='PEM')}")
print(f"\n\npublic key:\n{public_key.export_key(format='PEM')}")
print(f"\n\nencrypted text:\n{encrypted_text64}")


cipher = PKCS1_OAEP.new(private_key)
decrypted_text =cipher.decrypt(encrypted_text).decode("utf8")
print(f"\n\ndecrypted text:\n{decrypted_text}")