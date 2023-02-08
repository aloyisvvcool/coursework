from instagrapi import Client

# Create an instance of the Client class
cl = Client()

# Set the locale, country code, and timezone offset
cl.set_locale('en_US')
cl.set_country_code(65)  # +65
cl.set_timezone_offset(8 * 3600)  # Singapore UTC+8
cl.get_settings()
'''
# Aloysius, the login and password should be taken from the encrypted file
# And video path and caption
# Until then the user and pwd is plain text
'''
USERNAME = "plsgivea1"
PASSWORD = "43w tg534tgi537 bgv34"

# Log in to the account
try:
    cl.load_settings('/tmp/dump.json')
    cl.login(USERNAME, PASSWORD)
except:
    cl.login(USERNAME, PASSWORD)

# Store the session
cl.dump_settings('/tmp/dump.json')

# Check the session
cl.get_timeline_feed()

# Upload a video to the account
videopath = "/Users/snyper/Documents/samplevideo.mp4"
thumbnailpath = "/Users/snyper/Downloads/samplethumb.jpg"
caption = "testing"

cl.video_upload(videopath, caption, thumbnailpath)
