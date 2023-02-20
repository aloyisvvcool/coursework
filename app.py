'''
2023 Computing+ Coursework: Sociable
By: Aloysius (S4-01), Shrinithi (S4-01), Jonathan (S4=07)

Please read the readme and ensure that all required packages & libraries are installed
Note: Twitter posting will not work after 9 Feb 2023 since Twitter has made the Twitter API a paid service

Code done by Jonathan and Shri are indicated at the start and end of their respective parts
Other lines (except importing of packages & libraries) are done by Aloysius
'''

import tkinter  #tkinter and customtkinter are used for the app GUI
import customtkinter
from tkinter import filedialog as fd
from datetime import datetime   #time and datetime are used to check for time needed for posting
import time
from selenium import webdriver  #Selenium and pyautogui are used for posting on Tiktok and Instagram
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import tweepy   #used for Twitter posting. Has been deactivated since Feb 9 2023 when Twitter API was a made paid service :(
from cryptography.fernet import Fernet  #used for encrypting and decrypting passwords and other sensitive details
from google_auth_oauthlib.flow import InstalledAppFlow  #Google packages, pandas and os are needed for YouTUbe posting
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import pandas as pd
import os

def tobytes(x): #function to create bytes
    return bytes(x,'utf-8')

texts = []
with open('textinfo.txt','r') as f:
    [texts.append(line.strip()) for line in f.readlines()]

key = tobytes(texts[0])
fernet = Fernet(key) #casts key to needed type

TWITTER_ACCESS_KEY = fernet.decrypt(tobytes(texts[1])).decode() #creates usable strings from the encoded file
TWITTER_ACCESS_SECRET = fernet.decrypt(tobytes(texts[2])).decode()
TWITTER_CONSUMER_KEY = fernet.decrypt(tobytes(texts[3])).decode()
TWITTER_CONSUMER_SECRET = fernet.decrypt(tobytes(texts[4])).decode()
TIKTOK_EMAIL = fernet.decrypt(tobytes(texts[5])).decode()
TIKTOK_PASSWORD = fernet.decrypt(tobytes(texts[6])).decode()
INSTAGRAM_EMAIL = fernet.decrypt(tobytes(texts[7])).decode()
INSTAGRAM_PASSWORD = fernet.decrypt(tobytes(texts[8])).decode()
video_title = None  #These 5 variables are initialised, but should be changed later on
video_caption = None
upload_time = None
upload_date = None
file_path = None
customtkinter.set_appearance_mode("dark")  #this gets changed in the app
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x720")
app.title("Sociable")

def convert_number_to_date(number):
    date_string = datetime.strptime(number, '%d%m%Y').strftime('%d %B %Y')
    return date_string
def youtubecheck():
    print(youtubecb.get())

def twittercheck():
    print(twittercb.get())

def tiktokcheck():
    print(tiktokcb.get())

def instacheck():
    print(instacb.get())

titleadded = False
def titleadd():
    global titleadded
    global video_title
    if titleadded == True:
        destroy_title = lambda: title.destroy()
        destroy_title()
    title_name = title_entry.get()
    video_title = title_name
    global title
    title=customtkinter.CTkLabel(app, text=f'Title: {title_name}', font=('Helvetica', 15))
    title.place(x=70,y=300)
    titleadded = True

captionadded = False
def descriptionadd():
    global captionadded
    global video_caption
    if captionadded == True:
        destroy_caption = lambda: caption.destroy()
        destroy_caption()
    caption_name = caption_entry.get("1.0", 'end-1c')
    video_caption = caption_name
    global caption
    caption=customtkinter.CTkLabel(app, text=f'Caption: {caption_name}', font=('Helvetica', 15))
    caption.place(x=70,y=430)
    captionadded = True
    
timeadded = False
def timeadd():
    global upload_time
    time_str = time_entry.get()
    if not time_str.isdigit() or len(time_str) != 4:
        raise ValueError("Input should be a 4-digit time string in the format 'HHMM'")
    hour = int(time_str[:2])
    minute = int(time_str[2:])
    '''
    if hour == 0:
        hour = 12
        am_pm = "AM"
    elif hour < 12:
        am_pm = "AM"
    elif hour == 12:
        am_pm = "PM"
    else:
        hour -= 12
        am_pm = "PM"
    '''
    formatted_time = f"{hour}:{minute:02d}"

    global timeadded
    if timeadded == True:
        destroy_time = lambda: timevar.destroy()
        destroy_time()
    formatted_time = f"{hour}:{minute:02d}"
    upload_time = formatted_time
    global timevar
    timevar=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15))
    timevar.place(x=70,y=330)
    timeadded = True

dateadded = False
def dateadd():
    global upload_date
    day = date_entry.get()[:2]
    month = date_entry.get()[2:4]
    year = date_entry.get()[4:]
    upload_date = f"{day}/{month}/{year}"
    print(upload_date)
    global dateadded
    if dateadded == True:
        destroy_date = lambda: date.destroy()
        destroy_date()
    global date
    date=customtkinter.CTkLabel(app, text=f'Date: {upload_date}', font=('Helvetica', 15))
    date.place(x=70,y=360)
    dateadded = True

fileadded = False
def choose_file():
    file_path = str(fd.askopenfile())[25:-28]
    print(file_path)
    if len(file_path) > 30:
        file_path = file_path[:30] + "\n" + file_path[30:]
    global fileadded
    if fileadded == True:
        destroy_file = lambda: file.destroy()
        destroy_file()
    global file
    file=customtkinter.CTkLabel(app, text=f'File: {file_path}', font=('Helvetica', 15))
    file.place(x=70,y=390)
    fileadded = True

def post():
    global upload_date
    global upload_time
    date_time_str = str(upload_date) + " " + str(upload_time)
    end_time = time.strptime(date_time_str, "%d/%m/%Y %H:%M")
    while True:
        current_time = time.localtime()
        if current_time >= end_time:
            if youtubecb.get(): #youtube code here
                '''
                Start of Jonathan's Code
                '''
                def create_service(client_secret_file, api_name, api_version, *scopes, prefix=''):
                    CLIENT_SECRET_FILE = client_secret_file
                    API_SERVICE_NAME = api_name
                    API_VERSION = api_version
                    SCOPES = [scope for scope in scopes[0]]
                    
                    creds = None
                    working_dir = os.getcwd()
                    token_dir = 'token files'
                    token_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.json'

                    ### Check if token dir exists first, if not, create the folder
                    if not os.path.exists(os.path.join(working_dir, token_dir)):
                        os.mkdir(os.path.join(working_dir, token_dir))

                    if os.path.exists(os.path.join(working_dir, token_dir, token_file)):
                        creds = Credentials.from_authorized_user_file(os.path.join(working_dir, token_dir, token_file), SCOPES)
                        # with open(os.path.join(working_dir, token_dir, token_file), 'rb') as token:
                        #   cred = pickle.load(token)

                    if not creds or not creds.valid:
                        if creds and creds.expired and creds.refresh_token:
                            creds.refresh(Request())
                        else:
                            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                            creds = flow.run_local_server(port=0)

                        with open(os.path.join(working_dir, token_dir, token_file), 'w') as token:
                            token.write(creds.to_json())

                    try:
                        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds, static_discovery=False)
                        print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
                        return service
                    except Exception as e:
                        print(e)
                        print(f'Failed to create service instance for {API_SERVICE_NAME}')
                        os.remove(os.path.join(working_dir, token_dir, token_file))
                        return None

                def video_categories():
                    video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
                    df = pd.DataFrame(video_categories.get('items'))                                                #display information as a table
                    return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)                 #Return everything in a single view

                API_NAME = 'youtube'                                                                                #API used
                API_VERSION = 'v3'                                                                                  #Version
                SCOPES = ['https://www.googleapis.com/auth/youtube']                                                #Permission for anything youtuve related
                client_file = 'client-secret.json'
                service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

                #print(video_categories())
                upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'         #Upload date
                request_body = {
                    'snippet': {
                        'title': video_title,                                                                   #Insert title of video
                        'description': video_caption,                                                       #Insert video desciption
                        'categoryId': '26',                                                              #Insert category id
                        'tags': ['youtube api']                                                                            #Insert video tags
                    },
                    'status': {
                        'privacyStatus': 'private',                                                                 #Status privacy
                        'publishAt': upload_time,                                                                 #Post the video
                        'selfDeclaredMadeForKids': False                                                            #Kids?
                    },
                    'notifySubscribers': False                                                                      #Will the video notify subscibers
                }

                video_file = file_path                                                                       #Finds video file (mp4)
                media_file = MediaFileUpload(video_file)

                response_video_upload = service.videos().insert(                                                    #Gets video data
                    part='snippet,status',                                                                          #
                    body=request_body,                                                                              #
                    media_body=media_file                                                                           #
                ).execute()                                                                                         #
                uploaded_video_id = response_video_upload.get('id')    

                response_thumbnail_upload = service.thumbnails().set(                                               #Upload video thumbnail
                    videoId=uploaded_video_id,                                                                      #Uses video id to assign thumbnail
                    media_body=MediaFileUpload('thumbnail.png')                                                     #thumbnail being used
                ).execute()



                video_id = uploaded_video_id
                counter = 0
                response_update_video = service.videos().list(id=video_id, part='status').execute()                 #make api get video status
                update_video_body = response_update_video['items'][0]

                while 10 > counter:                                                                                 #Checks if the video is done processing before updating status to public
                    if update_video_body['status']['uploadStatus'] == 'processed':
                        update_video_body['status']['privacyStatus'] = 'public'
                        service.videos().update(
                            part='status',
                            body=update_video_body
                        ).execute()
                        print('Video {0} privacy status is updated to "{1}"'.format(update_video_body['id'], update_video_body['status']['privacyStatus']))
                        break

                    time.sleep(10)
                    response_update_video = service.videos().list(id=video_id, part='status').execute()
                    update_video_body = response_update_video['items'][0]
                    counter += 1 
                    '''
                    End of Jonathan's code
                    '''                                                                                   #Checks again every period of time 
            if twittercb.get(): #twitter code here
                    client = tweepy.Client(access_token=TWITTER_ACCESS_KEY,
                            access_token_secret=TWITTER_ACCESS_SECRET,
                            consumer_key=TWITTER_CONSUMER_KEY,
                            consumer_secret=TWITTER_CONSUMER_SECRET)
                    client.create_tweet(text=video_title,media_ids=file_path)
            if instacb.get():
                '''
                Start of Shri's Code
                '''
                # Create a new instance of the Edge driver
                driver = webdriver.Edge()

                # Navigate to Instagram website
                driver.get("https://www.instagram.com/")                             
                time.sleep(5)

                # Press the tab key 2 times
                for i in range(2):
                    pyautogui.press('tab')

                pyautogui.typewrite(INSTAGRAM_EMAIL)
                pyautogui.press('tab')
                pyautogui.typewrite(INSTAGRAM_PASSWORD)
                pyautogui.press('enter')

                time.sleep(10)
                # press the tab key 8 times
                for i in range(8):
                    pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(10)


                # Find the file input element and send the file path
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.hotkey('command', 'shift', 'g')
                time.sleep(2)
                pyautogui.typewrite(file_path)
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                for i in range(2):
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(2)
                for i in range(5):
                    pyautogui.press('tab')
                pyautogui.typewrite(video_caption)
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('enter')

                time.sleep(15)
                '''
                End of Shri's Code
                '''
            if tiktokcb.get():
                # Create a new instance of the Edge driver
                driver = webdriver.Edge()

                # Navigate to TikTok website
                driver.get("https://www.tiktok.com/")
                time.sleep(2)
                # Click on the login button
                login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
                login_button.click()

                time.sleep(1)
                # Press the tab key 3 times
                for i in range(3):
                    pyautogui.press('tab')

                # Press the enter key
                pyautogui.press('enter')

                for i in range(2):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                # Press the tab key 3 times
                for i in range(3):
                    pyautogui.press('tab')

                # Press the enter key
                pyautogui.press('enter')

                pyautogui.typewrite(TIKTOK_EMAIL)
                pyautogui.press('tab')
                pyautogui.typewrite(TIKTOK_PASSWORD)
                pyautogui.press('enter')

                time.sleep(10)

                ##########
                for i in range(8):
                    pyautogui.press('tab')
                pyautogui.typewrite(video_caption)
                for i in range(30):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.hotkey('command', 'shift', 'g')
                time.sleep(2)
                pyautogui.typewrite(file_path)
                time.sleep(2)
                pyautogui.press('enter')
                for i in range(33):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(10)
            time.sleep(60)
            break

def go_settings():
    def dark_mode_toggle():
        if dark_mode.get():
            customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
        else: 
            customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        print(customtkinter.get_appearance_mode())
    frame_1.destroy()
    global frame_2
    frame_2 = customtkinter.CTkFrame(master=app)
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)
    dark_mode = customtkinter.CTkSwitch(master=frame_2, command=dark_mode_toggle, text='Light Mode')
    dark_mode.place(x=70,y=100)
    if customtkinter.get_appearance_mode() == 'Light':
        dark_mode.select()
    heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30))
    heading.place(x=230,y=10)

    def updatekeys():
        TWITTER_ACCESS_KEY = textbox_TWITTER_ACCESS_KEY.get()
        TWITTER_ACCESS_SECRET = textbox_TWITTER_ACCESS_SECRET.get()
        TWITTER_CONSUMER_KEY = textbox_TWITTER_CONSUMER_KEY.get()
        TWITTER_CONSUMER_SECRET = textbox_TWITTER_ACCESS_SECRET.get()
        TIKTOK_EMAIL = textbox_TIKTOK_EMAIL.get()
        TIKTOK_PASSWORD = textbox_TIKTOK_PASSWORD.get()
        INSTAGRAM_EMAIL = textbox_INSTAGRAM_EMAIL.get()
        INSTAGRAM_PASSWORD = textbox_INSTAGRAM_PASSWORD.get()
        all_info = [
            TWITTER_ACCESS_KEY,
            TWITTER_ACCESS_SECRET,
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET,
            TIKTOK_EMAIL,
            TIKTOK_PASSWORD,
            INSTAGRAM_EMAIL,
            INSTAGRAM_PASSWORD
        ]
        key = Fernet.generate_key() #key generation, generates new keys each time
        fernet = Fernet(key) #cast key to fernet type
        
        with open('textinfo.txt','w') as f: #create txt file if it doesnt exist, and write to key
            f.write(str(key)[2:-1] + '\n')
            for i in all_info:
                encoded = fernet.encrypt(i.encode()) #encodes i
                f.write(str(encoded)[2:-1] + '\n')
            f.close()

    textbox_TWITTER_ACCESS_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Key")
    textbox_TWITTER_ACCESS_KEY.place(x=70,y=140)
    textbox_TWITTER_ACCESS_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Secret")
    textbox_TWITTER_ACCESS_SECRET.place(x=70,y=180)
    textbox_TWITTER_CONSUMER_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Key")
    textbox_TWITTER_CONSUMER_KEY.place(x=70,y=220)
    textbox_TWITTER_CONSUMER_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Secret")
    textbox_TWITTER_CONSUMER_SECRET.place(x=70,y=260)
    textbox_TIKTOK_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Email")
    textbox_TIKTOK_EMAIL.place(x=70,y=300)
    textbox_TIKTOK_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Password")
    textbox_TIKTOK_PASSWORD.place(x=70,y=340)
    textbox_INSTAGRAM_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Email")
    textbox_INSTAGRAM_EMAIL.place(x=70,y=380)
    textbox_INSTAGRAM_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Password")
    textbox_INSTAGRAM_PASSWORD.place(x=70,y=420)
    updateinfo = customtkinter.CTkButton(master=frame_2, command=updatekeys, text='Update Information')
    updateinfo.place(x=70,y=540)

    post = customtkinter.CTkButton(master=frame_2, command=go_post, text='Schedule Post')
    post.place(x=450,y=600)

def go_post(): #this is just every other line of code in this file (excluding library imports), but the code doesnt work without it
    def convert_number_to_date(number):
        date_string = datetime.strptime(number, '%d%m%Y').strftime('%d %B %Y')
        return date_string
    def youtubecheck():
        print(youtubecb.get())

    def twittercheck():
        print(twittercb.get())

    def tiktokcheck():
        print(tiktokcb.get())

    def instacheck():
        print(instacb.get())

    titleadded = False
    def titleadd():
        global titleadded
        if titleadded == True:
            destroy_title = lambda: title.destroy()
            destroy_title()
        title_name = title_entry.get()
        global title
        title=customtkinter.CTkLabel(app, text=f'Title: {title_name}', font=('Helvetica', 15))
        title.place(x=70,y=300)
        titleadded = True

    captionadded = False
    def descriptionadd():
        global captionadded
        if captionadded == True:
            destroy_caption = lambda: caption.destroy()
            destroy_caption()
        caption_name = caption_entry.get("1.0", 'end-1c')
        global caption
        caption=customtkinter.CTkLabel(app, text=f'Caption: {caption_name}', font=('Helvetica', 15))
        caption.place(x=70,y=430)
        captionadded = True
            
    timeadded = False
    def timeadd():
        global upload_time
        time_str = time_entry.get()
        if not time_str.isdigit() or len(time_str) != 4:
            raise ValueError("Input should be a 4-digit time string in the format 'HHMM'")
        hour = int(time_str[:2])
        minute = int(time_str[2:])
        '''
        if hour == 0:
            hour = 12
            am_pm = "AM"
        elif hour < 12:
            am_pm = "AM"
        elif hour == 12:
            am_pm = "PM"
        else:
            hour -= 12
            am_pm = "PM"
        '''
        formatted_time = f"{hour}:{minute:02d}"

        global timeadded
        if timeadded == True:
            destroy_time = lambda: timevar.destroy()
            destroy_time()
        formatted_time = f"{hour}:{minute:02d}"
        upload_time = formatted_time
        global timevar
        timevar=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15))
        timevar.place(x=70,y=330)
        timeadded = True

    dateadded = False
    def dateadd():
        global upload_date
        day = date_entry.get()[:2]
        month = date_entry.get()[2:4]
        year = date_entry.get()[4:]
        upload_date = f"{day}/{month}/{year}"
        print(upload_date)
        global dateadded
        if dateadded == True:
            destroy_date = lambda: date.destroy()
            destroy_date()
        global date
        date=customtkinter.CTkLabel(app, text=f'Date: {upload_date}', font=('Helvetica', 15))
        date.place(x=70,y=360)
        dateadded = True

    fileadded = False
    def choose_file():
        file_path = str(fd.askopenfile())[25:-28]
        print(file_path)
        if len(file_path) > 30:
            file_path = file_path[:30] + "\n" + file_path[30:]
        global fileadded
        if fileadded == True:
            destroy_file = lambda: file.destroy()
            destroy_file()
        global file
        file=customtkinter.CTkLabel(app, text=f'File: {file_path}', font=('Helvetica', 15))
        file.place(x=70,y=390)
        fileadded = True

    def post():
        global upload_date
        global upload_time
        date_time_str = str(upload_date) + " " + str(upload_time)
        end_time = time.strptime(date_time_str, "%d/%m/%Y %H:%M")
        while True:
            current_time = time.localtime()
            if current_time >= end_time:
                if youtubecb.get(): #youtube code here
                    '''
                    Start of Jonathan's Code
                    '''
                    def create_service(client_secret_file, api_name, api_version, *scopes, prefix=''):
                        CLIENT_SECRET_FILE = client_secret_file
                        API_SERVICE_NAME = api_name
                        API_VERSION = api_version
                        SCOPES = [scope for scope in scopes[0]]
                        
                        creds = None
                        working_dir = os.getcwd()
                        token_dir = 'token files'
                        token_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.json'

                        ### Check if token dir exists first, if not, create the folder
                        if not os.path.exists(os.path.join(working_dir, token_dir)):
                            os.mkdir(os.path.join(working_dir, token_dir))

                        if os.path.exists(os.path.join(working_dir, token_dir, token_file)):
                            creds = Credentials.from_authorized_user_file(os.path.join(working_dir, token_dir, token_file), SCOPES)
                            # with open(os.path.join(working_dir, token_dir, token_file), 'rb') as token:
                            #   cred = pickle.load(token)

                        if not creds or not creds.valid:
                            if creds and creds.expired and creds.refresh_token:
                                creds.refresh(Request())
                            else:
                                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                                creds = flow.run_local_server(port=0)

                            with open(os.path.join(working_dir, token_dir, token_file), 'w') as token:
                                token.write(creds.to_json())

                        try:
                            service = build(API_SERVICE_NAME, API_VERSION, credentials=creds, static_discovery=False)
                            print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
                            return service
                        except Exception as e:
                            print(e)
                            print(f'Failed to create service instance for {API_SERVICE_NAME}')
                            os.remove(os.path.join(working_dir, token_dir, token_file))
                            return None

                    def video_categories():
                        video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
                        df = pd.DataFrame(video_categories.get('items'))                                                #display information as a table
                        return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)                 #Return everything in a single view

                    API_NAME = 'youtube'                                                                                #API used
                    API_VERSION = 'v3'                                                                                  #Version
                    SCOPES = ['https://www.googleapis.com/auth/youtube']                                                #Permission for anything youtuve related
                    client_file = 'client-secret.json'
                    service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

                    #print(video_categories())
                    upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'         #Upload date
                    request_body = {
                        'snippet': {
                            'title': video_title,                                                                   #Insert title of video
                            'description': video_caption,                                                       #Insert video desciption
                            'categoryId': '26',                                                              #Insert category id
                            'tags': ['youtube api']                                                                            #Insert video tags
                        },
                        'status': {
                            'privacyStatus': 'private',                                                                 #Status privacy
                            'publishAt': upload_time,                                                                 #Post the video
                            'selfDeclaredMadeForKids': False                                                            #Kids?
                        },
                        'notifySubscribers': False                                                                      #Will the video notify subscibers
                    }

                    video_file = file_path                                                                       #Finds video file (mp4)
                    media_file = MediaFileUpload(video_file)

                    response_video_upload = service.videos().insert(                                                    #Gets video data
                        part='snippet,status',                                                                          #
                        body=request_body,                                                                              #
                        media_body=media_file                                                                           #
                    ).execute()                                                                                         #
                    uploaded_video_id = response_video_upload.get('id')    

                    response_thumbnail_upload = service.thumbnails().set(                                               #Upload video thumbnail
                        videoId=uploaded_video_id,                                                                      #Uses video id to assign thumbnail
                        media_body=MediaFileUpload('thumbnail.png')                                                     #thumbnail being used
                    ).execute()



                    video_id = uploaded_video_id
                    counter = 0
                    response_update_video = service.videos().list(id=video_id, part='status').execute()                 #make api get video status
                    update_video_body = response_update_video['items'][0]

                    while 10 > counter:                                                                                 #Checks if the video is done processing before updating status to public
                        if update_video_body['status']['uploadStatus'] == 'processed':
                            update_video_body['status']['privacyStatus'] = 'public'
                            service.videos().update(
                                part='status',
                                body=update_video_body
                            ).execute()
                            print('Video {0} privacy status is updated to "{1}"'.format(update_video_body['id'], update_video_body['status']['privacyStatus']))
                            break

                        time.sleep(10)
                        response_update_video = service.videos().list(id=video_id, part='status').execute()
                        update_video_body = response_update_video['items'][0]
                        counter += 1  
                        '''
                        End of Jonathan's Code
                        '''                                                                                  #Checks again every period of time 
                if twittercb.get(): #twitter code here
                        client = tweepy.Client(access_token=TWITTER_ACCESS_KEY,
                                access_token_secret=TWITTER_ACCESS_SECRET,
                                consumer_key=TWITTER_CONSUMER_KEY,
                                consumer_secret=TWITTER_CONSUMER_SECRET)
                        client.create_tweet(text=video_title,media_ids=file_path)
                if instacb.get():
                    '''
                    Start of Shri's Code
                    '''
                    # Create a new instance of the Edge driver
                    driver = webdriver.Edge()

                    # Navigate to Instagram website
                    driver.get("https://www.instagram.com/")                             
                    time.sleep(5)

                    # Press the tab key 2 times
                    for i in range(2):
                        pyautogui.press('tab')

                    pyautogui.typewrite(INSTAGRAM_EMAIL)
                    pyautogui.press('tab')
                    pyautogui.typewrite(INSTAGRAM_PASSWORD)
                    pyautogui.press('enter')

                    time.sleep(10)
                    # press the tab key 8 times
                    for i in range(8):
                        pyautogui.press('tab')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(10)


                    # Find the file input element and send the file path
                    pyautogui.press('tab')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.hotkey('command', 'shift', 'g')
                    time.sleep(2)
                    pyautogui.typewrite(file_path)
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(2)
                    for i in range(2):
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        time.sleep(2)
                    for i in range(5):
                        pyautogui.press('tab')
                    pyautogui.typewrite(video_caption)
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.press('enter')

                    time.sleep(15)
                    '''
                    End of Shri's Code
                    '''
                if tiktokcb.get():
                    # Create a new instance of the Edge driver
                    driver = webdriver.Edge()

                    # Navigate to TikTok website
                    driver.get("https://www.tiktok.com/")
                    time.sleep(2)
                    # Click on the login button
                    login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
                    login_button.click()

                    time.sleep(1)
                    # Press the tab key 3 times
                    for i in range(3):
                        pyautogui.press('tab')

                    # Press the enter key
                    pyautogui.press('enter')

                    for i in range(2):
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    # Press the tab key 3 times
                    for i in range(3):
                        pyautogui.press('tab')

                    # Press the enter key
                    pyautogui.press('enter')

                    pyautogui.typewrite(TIKTOK_EMAIL)
                    pyautogui.press('tab')
                    pyautogui.typewrite(TIKTOK_PASSWORD)
                    pyautogui.press('enter')

                    time.sleep(10)

                    ##########
                    for i in range(8):
                        pyautogui.press('tab')
                    pyautogui.typewrite(video_caption)
                    for i in range(30):
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    pyautogui.hotkey('command', 'shift', 'g')
                    time.sleep(2)
                    pyautogui.typewrite(file_path)
                    time.sleep(2)
                    pyautogui.press('enter')
                    for i in range(33):
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(10)
                time.sleep(60)
                break

    def go_settings():
        def dark_mode_toggle():
            if dark_mode.get():
                customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
            else: 
                customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
            print(customtkinter.get_appearance_mode())
        frame_1.destroy()
        global frame_2
        frame_2 = customtkinter.CTkFrame(master=app)
        frame_2.pack(pady=20, padx=60, fill="both", expand=True)
        dark_mode = customtkinter.CTkSwitch(master=frame_2, command=dark_mode_toggle, text='Light Mode')
        dark_mode.place(x=70,y=100)
        if customtkinter.get_appearance_mode() == 'Light':
            dark_mode.select()
        heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30))
        heading.place(x=230,y=10)

        def updatekeys():
            TWITTER_ACCESS_KEY = textbox_TWITTER_ACCESS_KEY.get()
            TWITTER_ACCESS_SECRET = textbox_TWITTER_ACCESS_SECRET.get()
            TWITTER_CONSUMER_KEY = textbox_TWITTER_CONSUMER_KEY.get()
            TWITTER_CONSUMER_SECRET = textbox_TWITTER_ACCESS_SECRET.get()
            TIKTOK_EMAIL = textbox_TIKTOK_EMAIL.get()
            TIKTOK_PASSWORD = textbox_TIKTOK_PASSWORD.get()
            INSTAGRAM_EMAIL = textbox_INSTAGRAM_EMAIL.get()
            INSTAGRAM_PASSWORD = textbox_INSTAGRAM_PASSWORD.get()
            all_info = [
                TWITTER_ACCESS_KEY,
                TWITTER_ACCESS_SECRET,
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET,
                TIKTOK_EMAIL,
                TIKTOK_PASSWORD,
                INSTAGRAM_EMAIL,
                INSTAGRAM_PASSWORD
            ]
            key = Fernet.generate_key() #key generation, generates new keys each time
            fernet = Fernet(key) #cast key to fernet type
            
            with open('textinfo.txt','w') as f: #create txt file if it doesnt exist, and write to key
                f.write(str(key)[2:-1] + '\n')
                for i in all_info:
                    encoded = fernet.encrypt(i.encode()) #encodes i
                    f.write(str(encoded)[2:-1] + '\n')
                f.close()

        textbox_TWITTER_ACCESS_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Key")
        textbox_TWITTER_ACCESS_KEY.place(x=70,y=140)
        textbox_TWITTER_ACCESS_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Secret")
        textbox_TWITTER_ACCESS_SECRET.place(x=70,y=180)
        textbox_TWITTER_CONSUMER_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Key")
        textbox_TWITTER_CONSUMER_KEY.place(x=70,y=220)
        textbox_TWITTER_CONSUMER_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Secret")
        textbox_TWITTER_CONSUMER_SECRET.place(x=70,y=260)
        textbox_TIKTOK_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Email")
        textbox_TIKTOK_EMAIL.place(x=70,y=300)
        textbox_TIKTOK_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Password")
        textbox_TIKTOK_PASSWORD.place(x=70,y=340)
        textbox_INSTAGRAM_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Email")
        textbox_INSTAGRAM_EMAIL.place(x=70,y=380)
        textbox_INSTAGRAM_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Password")
        textbox_INSTAGRAM_PASSWORD.place(x=70,y=420)
        updateinfo = customtkinter.CTkButton(master=frame_2, command=updatekeys, text='Update Information')
        updateinfo.place(x=70,y=540)

        post = customtkinter.CTkButton(master=frame_2, command=go_post, text='Schedule Post')
        post.place(x=450,y=600)


    frame_2.destroy()
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title")
    title_entry.place(x=300,y=70)
    title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title')
    title_confirm.place(x=300,y=110)

    caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200)
    caption_entry.place(x=300,y=160)
    caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description')
    caption_confirm.place(x=300,y=370)

    time_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="HHMM")
    time_entry.place(x=300,y=420)
    time_confirm = customtkinter.CTkButton(master=frame_1, command=timeadd, text='Add Time')
    time_confirm.place(x=300,y=460)

    date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY")
    date_entry.place(x=300,y=510)
    date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date')
    date_confirm.place(x=300,y=550)

    file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select Video File')
    file_select.place(x=300,y=590)

    post_button = customtkinter.CTkButton(master=frame_1, command=post, text='Schedule!')
    post_button.place(x=300,y=630)

    heading = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post', font=('Helvetica', 30))
    heading.place(x=230,y=10)

    youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube', font=('Helvetica', 20))
    youtubecb.place(x=70,y=70)

    twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter', font=('Helvetica', 20))
    twittercb.place(x=70,y=120)

    tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok', font=('Helvetica', 20))
    tiktokcb.place(x=70,y=170)

    instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram', font=('Helvetica', 20))
    instacb.place(x=70,y=220)

    settings = customtkinter.CTkButton(master=frame_1, command=go_settings, text='Settings')
    settings.place(x=450,y=600)

    app.mainloop()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title")
title_entry.place(x=300,y=70)
title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title')
title_confirm.place(x=300,y=110)

caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200)
caption_entry.place(x=300,y=160)
caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description')
caption_confirm.place(x=300,y=370)

time_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="HHMM")
time_entry.place(x=300,y=420)
time_confirm = customtkinter.CTkButton(master=frame_1, command=timeadd, text='Add Time')
time_confirm.place(x=300,y=460)

date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY")
date_entry.place(x=300,y=510)
date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date')
date_confirm.place(x=300,y=550)

file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select Video File')
file_select.place(x=300,y=590)

post_button = customtkinter.CTkButton(master=frame_1, command=post, text='Schedule!')
post_button.place(x=300,y=630)

heading = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post', font=('Helvetica', 30))
heading.place(x=230,y=10)

youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube', font=('Helvetica', 20))
youtubecb.place(x=70,y=70)

twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter', font=('Helvetica', 20))
twittercb.place(x=70,y=120)

tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok', font=('Helvetica', 20))
tiktokcb.place(x=70,y=170)

instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram', font=('Helvetica', 20))
instacb.place(x=70,y=220)

settings = customtkinter.CTkButton(master=frame_1, command=go_settings, text='Settings')
settings.place(x=450,y=600)

app.mainloop()