import hashlib 
plain_text="hello"

md5 = hashlib.md5(plain_text.encode("utf8")).hexdigest()
sha256 = hashlib.sha256(plain_text.encode("utf8")).hexdigest()

print(md5)
print(sha256)
