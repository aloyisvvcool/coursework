from cryptography.fernet import Fernet

def tobytes(x):
    return bytes(x,'utf-8')

texts = []
with open('textinfo.txt','r') as f:
    [texts.append(line.strip()) for line in f.readlines()]
print(texts)

key = tobytes(texts[0])
msg = tobytes(texts[1])
fernet = Fernet(key) #casts key to needed type

text = fernet.decrypt(msg).decode() # decodes message into usable string
 
print("decrypted string: ", text)
