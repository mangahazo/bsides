from Crypto.Cipher import AES


with open('fake.png', 'rb') as f:
    data = f.read()


cipher = AES.new(b'sup3rrr s3cr3ttt', AES.MODE_CTR)

encrypted = cipher.encrypt(data)

# print(cipher.nonce)
with open('fake.png.enc', 'wb') as f:
    f.write(encrypted)
    
