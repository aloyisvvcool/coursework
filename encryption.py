from cryptography.fernet import Fernet
 
# we will be encrypting the below string.
message = "pissandcum"

key = Fernet.generate_key() #key generation, generates new keys each time
fernet = Fernet(key) #cast key to fernet tye
# Instance the Fernet class with the key
print(bytes(str(key)[2:-1], 'utf-8'))
print(str(key))
print(key)
print(type(key))

encMessage = fernet.encrypt(message.encode()) #encode
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
with open('fernk.txt','w') as f: #create txt file if it doesnt exist, and write to key
    f.write(str(key)[2:-1])
    f.close()
with open('msg.txt','w') as g: #create txt file if it doesnt exist, and write to key
    g.write(str(encMessage)[2:-1])
    g.close()
