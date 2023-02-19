from cryptography.fernet import Fernet

def tobytes(x):
    return bytes(x,'utf-8')

texts = []
with open('textinfo.txt','r') as f:
    [texts.append(line.strip()) for line in f.readlines()]

key = tobytes(texts[0])
fernet = Fernet(key) #casts key to needed type

TWITTER_ACCESS_KEY = fernet.decrypt(tobytes(texts[1])).decode() #creates usable strings
TWITTER_ACCESS_SECRET = fernet.decrypt(tobytes(texts[2])).decode()
TWITTER_CONSUMER_KEY = fernet.decrypt(tobytes(texts[3])).decode()
TWITTER_CONSUMER_SECRET = fernet.decrypt(tobytes(texts[4])).decode()
TIKTOK_EMAIL = fernet.decrypt(tobytes(texts[5])).decode()
TIKTOK_PASSWORD = fernet.decrypt(tobytes(texts[6])).decode()
YOUTUBE_CLIENT = fernet.decrypt(tobytes(texts[7])).decode()
YOUTUBE_SECRET = fernet.decrypt(tobytes(texts[8])).decode()
INSTAGRAM_EMAIL = fernet.decrypt(tobytes(texts[9])).decode()
INSTAGRAM_PASSWORD = fernet.decrypt(tobytes(texts[10])).decode()