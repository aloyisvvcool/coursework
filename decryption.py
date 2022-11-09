from cryptography.fernet import Fernet

with open('fernk.txt','r') as f:
    key = bytes(str(f.readlines()),'utf-8')
with open('msg.txt','r') as f:
    msg = bytes(str(f.readlines()),'utf-8')
fernet = Fernet(key)
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(msg).decode()
 
print("decrypted string: ", decMessage)