from cryptography.fernet import Fernet
 
# we will be encrypting the below strings
TWITTER_ACCESS_KEY = ""
TWITTER_ACCESS_SECRET = ""
TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TIKTOK_EMAIL = ""
TIKTOK_PASSWORD = ""
YOUTUBE_CLIENT = ""
YOUTUBE_SECRET = ""
INSTAGRAM_EMAIL = ""
INSTAGRAM_PASSWORD = ""
all_info = [
    TWITTER_ACCESS_KEY,
    TWITTER_ACCESS_SECRET,
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TIKTOK_EMAIL,
    TIKTOK_PASSWORD,
    YOUTUBE_CLIENT,
    YOUTUBE_SECRET,
    INSTAGRAM_EMAIL,
    INSTAGRAM_PASSWORD
]
key = Fernet.generate_key() #key generation, generates new keys each time
fernet = Fernet(key) #cast key to fernet tye
 
with open('textinfo.txt','w') as f: #create txt file if it doesnt exist, and write to key
    f.write(str(key)[2:-1] + '\n')
    for i in all_info:
        encoded = fernet.encrypt(i.encode()) #encodes i
        f.write(str(encoded)[2:-1] + '\n')
    f.close()
