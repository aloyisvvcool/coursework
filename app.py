'''

2023 Computing+ Coursework: Sociable - A Social Media Posting App
By: Aloysius (S4-01), Shrinithi (S4-01), Jonathan (S4-07) 

Please read the README.md file for more information about this project and how to use it.
Please ensure that all required packages & libraries are installed before running this app.
Note: Twitter posting will not work after 9 Feb 2023 since Twitter has made the Twitter API a paid service (https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).

Code done by Jonathan and Shrinithi are indicated at the start and end of their respective parts.
Other lines (except importing of packages & libraries) are done by Aloysius.

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

def tobytes(x): #function used in decrypting information from file
    return bytes(x,'utf-8')

texts = []  #contains all the encrypted files
with open('textinfo.txt','r') as f: #opens the file
    [texts.append(line.strip()) for line in f.readlines()] #reads the file and adds each line to the list

key = tobytes(texts[0]) #gets the key from the file
fernet = Fernet(key) #casts key to needed type

TWITTER_ACCESS_KEY = fernet.decrypt(tobytes(texts[1])).decode() #decodes the strings, the .decode() is needed since the strings are encrypted as bytes, this line for twitter access key
TWITTER_ACCESS_SECRET = fernet.decrypt(tobytes(texts[2])).decode() #same as above, but for twitter access secret
TWITTER_CONSUMER_KEY = fernet.decrypt(tobytes(texts[3])).decode() #same as above, but for twitter consumer key
TWITTER_CONSUMER_SECRET = fernet.decrypt(tobytes(texts[4])).decode() #same as above, but for twitter consumer secret
TIKTOK_EMAIL = fernet.decrypt(tobytes(texts[5])).decode() #same as above, but for tiktok email
TIKTOK_PASSWORD = fernet.decrypt(tobytes(texts[6])).decode() #same as above, but for tiktok password
INSTAGRAM_EMAIL = fernet.decrypt(tobytes(texts[7])).decode() #same as above, but for instagram email
INSTAGRAM_PASSWORD = fernet.decrypt(tobytes(texts[8])).decode() #same as above, but for instagram password
video_title = None  #These 5 variables are initialised, but should be changed later on
video_caption = None
upload_time = None
upload_date = None
file_path = None #initialising file_path is especially important for the tiktok code to work properly
customtkinter.set_appearance_mode("dark")  #sets the app to dark mode, but can get changed in the app
customtkinter.set_default_color_theme("blue")   #sets the theme of the app

app = customtkinter.CTk()
app.geometry("720x720") #sets the dimensions of the app window
app.title("Sociable") #sets the app name to "Sociable"

def convert_number_to_date(number): #function that converts the date entered into a string
    date_string = datetime.strptime(number, '%d%m%Y').strftime('%d %B %Y') #converts the date into a string
    return date_string #returns the string

def youtubecheck(): #function that checks if the youtube box is ticked, is empty since we don't use it but is needed to create the checkbox
    pass

def twittercheck(): #function that checks if the twitter box is ticked, is empty since we don't use it but is needed to create the checkbox
    pass

def tiktokcheck(): #function that checks if the tiktok box is ticked, is empty since we don't use it but is needed to create the checkbox
    pass

def instacheck(): #function that checks if the instagram box is ticked, is empty since we don't use it but is needed to create the checkbox
    pass

titleadded = False  #placeholder variable, only there so that title can be displayed once entered
def titleadd(): #function that adds the title to the app
    global titleadded #makes the variable global so that it can be used outside of the function
    global video_title #makes the variable global so that it can be used outside of the function
    if titleadded == True: #if a title has been previously added, remove it
        destroy_title = lambda: title.destroy()
        destroy_title() #removes the title
    title_name = title_entry.get() #assign the title that has been entered to variable
    video_title = title_name #assign the title that has been entered to
    global title #makes the variable global so that it can be used outside of the function
    title=customtkinter.CTkLabel(app, text=f'Title: {title_name}', font=('Helvetica', 15)) #create the label for the title
    title.place(x=70,y=300) #place the label
    titleadded = True #makes the variable true so that the title can't be added again

captionadded = False #placeholder variable, only there so that caption can be displayed once entered
def descriptionadd(): #function that adds the caption to the app
    global captionadded #makes the variable global so that it can be used outside of the function
    global video_caption #makes the variable global so that it can be used outside of the function
    if captionadded == True: #if a caption has been previously added, remove it
        destroy_caption = lambda: caption.destroy()
        destroy_caption() #removes the caption
    caption_name = caption_entry.get("1.0", 'end-1c') #assign the caption that has been entered to variable
    video_caption = caption_name #assign the caption that has been entered to
    global caption #makes the variable global so that it can be used outside of the function
    caption=customtkinter.CTkLabel(app, text=f'Caption: {caption_name}', font=('Helvetica', 15)) #create the label for the caption
    caption.place(x=70,y=430) #place the label
    captionadded = True #makes the variable true so that the caption can't be added again
    
timeadded = False #placeholder variable, only there so that time can be displayed once entered
def timeadd(): #function that adds the time to the app
    global upload_time #makes the variable global so that it can be used outside of the function
    time_str = time_entry.get() #assign the time that has been entered to variable
    if not time_str.isdigit() or len(time_str) != 4: #if the time does not fit the needed format of HHMM, reject it
        raise ValueError("Input should be a 4-digit time string in the format 'HHMM'") #raise an error
    else: #if the time is in the correct format, format it
        hour = int(time_str[:2]) #formats the time input into a usable string
        minute = int(time_str[2:]) #formats the time input into a usable string
        formatted_time = f"{hour}:{minute:02d}" #formats the time input into a usable string

    global timeadded #makes the variable global so that it can be used outside of the function
    if timeadded == True: #if a time has been previously added, remove it
        destroy_time = lambda: timevar.destroy()
        destroy_time() #removes the time
    formatted_time = f"{hour}:{minute:02d}" #formats the time input into a usable string
    upload_time = formatted_time #assign the time that has been entered to
    global timevar #makes the variable global so that it can be used outside of the function
    timevar=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15)) #create the label for the time
    timevar.place(x=70,y=330) #place the label
    timeadded = True

dateadded = False #placeholder variable, only there so that date can be displayed once entered
def dateadd():
    global upload_date #makes the variable global so that it can be used outside of the function
    day = date_entry.get()[:2] #assign the date that has been entered to variables based on day, month and year
    month = date_entry.get()[2:4] 
    year = date_entry.get()[4:]
    upload_date = f"{day}/{month}/{year}" #create a usable string and assign it to variable
    global dateadded
    if dateadded == True: #if a date has been previously added, remove it
        destroy_date = lambda: date.destroy()
        destroy_date() #removes the date
    global date #makes the variable global so that it can be used outside of the function
    date=customtkinter.CTkLabel(app, text=f'Date: {upload_date}', font=('Helvetica', 15)) #create the date for the time
    date.place(x=70,y=360) #place the label
    dateadded = True #makes the variable true so that the date can't be added again

fileadded = False #placeholder variable, only there so that file path can be displayed once entered
def choose_file():
    file_path = str(fd.askopenfile())[25:-28] #gets the file path of the file that has been selected
    print(file_path) #prints the file path to the console
    if len(file_path) > 25: #if the file path exceeds 25 characters, use the next line
        file_path = file_path[:25] + "\n" + file_path[25:]
    global fileadded #makes the variable global so that it can be used outside of the function
    if fileadded == True: #if a file has been previously added, remove it
        destroy_file = lambda: file.destroy()
        destroy_file() #removes the file path
    global file #makes the variable global so that it can be used outside of the function
    file=customtkinter.CTkLabel(app, text=f'File: {file_path}', font=('Helvetica', 15)) #create the date for the file path
    file.place(x=70,y=390) #place the label
    fileadded = True #makes the variable true so that the file path can't be added again

def post(): #function to check if the set time has passed, and then post on various platforms
    global upload_date #makes the variable global so that it can be used outside of the function
    global upload_time
    date_time_str = str(upload_date) + " " + str(upload_time) 
    end_time = time.strptime(date_time_str, "%d/%m/%Y %H:%M") #formats the date and time into a usable string
    while True: #while loop to check if the time has passed
        current_time = time.localtime() #gets the current time
        if current_time >= end_time: #if the time has passed, post on the platforms
            if youtubecb.get(): #posts video on youtube
                '''
                Start of Jonathan's Code
                '''
                def create_service(client_secret_file, api_name, api_version, *scopes, prefix=''): #function to create a service
                    CLIENT_SECRET_FILE = client_secret_file #assign the client secret file to a variable
                    API_SERVICE_NAME = api_name #assign the api name to a variable
                    API_VERSION = api_version #assign the api version to a variable
                    SCOPES = [scope for scope in scopes[0]] #assign the scopes to a variable
                    
                    creds = None #assign the credentials to a variable
                    working_dir = os.getcwd() #assign the working directory to a variable
                    token_dir = 'token files' #assign the token directory to a variable
                    token_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.json' #assign the token file to a variable

                    ### Check if token dir exists first, if not, create the folder
                    if not os.path.exists(os.path.join(working_dir, token_dir)):
                        os.mkdir(os.path.join(working_dir, token_dir))

                    if os.path.exists(os.path.join(working_dir, token_dir, token_file)):
                        creds = Credentials.from_authorized_user_file(os.path.join(working_dir, token_dir, token_file), SCOPES)
                        # with open(os.path.join(working_dir, token_dir, token_file), 'rb') as token:
                        #   cred = pickle.load(token)

                    if not creds or not creds.valid: #if the credentials are invalid, refresh them
                        if creds and creds.expired and creds.refresh_token: #if the credentials are expired, refresh them
                            creds.refresh(Request()) #refresh the credentials
                        else:
                            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES) #create the flow
                            creds = flow.run_local_server(port=0) #run the flow

                        with open(os.path.join(working_dir, token_dir, token_file), 'w') as token: #save the credentials
                            token.write(creds.to_json()) #write the credentials to the token file

                    try:
                        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds, static_discovery=False) #create the service
                        print(API_SERVICE_NAME, API_VERSION, 'service created successfully') #if the service is created, print this
                        return service #return the service
                    except Exception as e: #if the service fails to create, print the error
                        print(e) #print the error
                        print(f'Failed to create service instance for {API_SERVICE_NAME}') #if the service fails to create, print this
                        os.remove(os.path.join(working_dir, token_dir, token_file)) #remove the token file
                        return None

                def video_categories():
                    video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()    #Get video categories
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
                    part='snippet,status',                                                                          #Parts of the video
                    body=request_body,                                                                              #Body of the video
                    media_body=media_file                                                                           #Media of the video
                ).execute()                                                                                         #Execute the video
                uploaded_video_id = response_video_upload.get('id')                                                 #Get the video id

                response_thumbnail_upload = service.thumbnails().set(                                               #Upload video thumbnail
                    videoId=uploaded_video_id,                                                                      #Uses video id to assign thumbnail
                    media_body=MediaFileUpload('thumbnail.png')                                                     #thumbnail being used
                ).execute()                                                                                         #Execute the thumbnail



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
            if twittercb.get(): #posts video on twitter
                    client = tweepy.Client(access_token=TWITTER_ACCESS_KEY, #create a client that needs 4 API credentials
                            access_token_secret=TWITTER_ACCESS_SECRET,
                            consumer_key=TWITTER_CONSUMER_KEY,
                            consumer_secret=TWITTER_CONSUMER_SECRET)
                    client.create_tweet(text=video_title,media_ids=file_path) #post a tweet, with the title and video
            if instacb.get(): #posts video on instagram
                '''
                Start of Shrinithi's Code
                '''
                # Create a new instance of the Edge driver
                driver = webdriver.Edge()

                # Navigate to Instagram website
                driver.get("https://www.instagram.com/")                             
                time.sleep(10) #wait for the page to load

                # Press the tab key 2 times to move to the email field
                for i in range(2):
                    pyautogui.press('tab')

                pyautogui.typewrite(INSTAGRAM_EMAIL) #type in the email
                pyautogui.press('tab') #press tab to move to the password field
                pyautogui.typewrite(INSTAGRAM_PASSWORD) #type in the password
                pyautogui.press('enter') #press enter to login

                time.sleep(10) #wait for the page to load
                # press the tab key 8 times to navigate to the create button
                for i in range(8):
                    pyautogui.press('tab')
                time.sleep(2) #wait for the page to load
                pyautogui.press('enter') #press enter to create a post
                time.sleep(10) #wait for the page to load

                pyautogui.press('tab') #press tab to move to the file input element
                time.sleep(2)
                pyautogui.press('enter') #press enter to open the file explorer
                time.sleep(2)
                pyautogui.hotkey('command', 'shift', 'g') #open the go to folder dialog
                time.sleep(2)
                pyautogui.typewrite(file_path) #type in the file path
                time.sleep(2)
                pyautogui.press('enter') #press enter to open the file
                time.sleep(2)
                for i in range(2): #press tab 2 times to move to the next button
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(2)
                for i in range(5): #press tab 5 times to move to the caption field
                    pyautogui.press('tab')
                pyautogui.typewrite(video_caption) #type in the caption
                pyautogui.hotkey('shift', 'tab') #press shift + tab to move to the next button
                pyautogui.hotkey('shift', 'tab') #press shift + tab to move to the next button
                pyautogui.press('enter') #press enter to post the video

                time.sleep(15) #wait for the page to load
                '''
                End of Shrinithi's Code
                '''
            if tiktokcb.get(): #posts video on tiktok
                # Create a new instance of the Edge driver
                driver = webdriver.Edge()

                # Navigate to TikTok website
                driver.get("https://www.tiktok.com/")
                time.sleep(2)
                # Click on the login button
                login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
                login_button.click()

                time.sleep(1)
                for i in range(3): # navigate to the login page
                    pyautogui.press('tab')
                pyautogui.press('enter')
                for i in range(2): #logs into the account
                    pyautogui.press('tab')
                pyautogui.press('enter')
                for i in range(3):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.typewrite(TIKTOK_EMAIL)
                pyautogui.press('tab')
                pyautogui.typewrite(TIKTOK_PASSWORD)
                pyautogui.press('enter')

                time.sleep(5)

                for i in range(8): #enters video information and posts the video
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
                for i in range(33): #33 looks like a lot, but its intentional
                    pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(10)
            time.sleep(60) #wait for the next minute if the time has not come
            break

def go_settings():
    def dark_mode_toggle():
        if dark_mode.get(): #set the app to light mode if indicated, if not stick with dark mode
            customtkinter.set_appearance_mode("light")
        else: 
            customtkinter.set_appearance_mode("dark")

    def updatekeys(): #function to update account information in the file
        TWITTER_ACCESS_KEY = textbox_TWITTER_ACCESS_KEY.get() #assigns the information in the textbox to a corresponding variable
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
                encoded = fernet.encrypt(i.encode()) #encodes every line
                f.write(str(encoded)[2:-1] + '\n')
            f.close()
    frame_1.destroy() #removes the previous page frame
    global frame_2
    frame_2 = customtkinter.CTkFrame(master=app) #creates a new page frame
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)
    dark_mode = customtkinter.CTkSwitch(master=frame_2, command=dark_mode_toggle, text='Light Mode') #creates a toggle switch for the dark/light mdoe
    dark_mode.place(x=70,y=100)
    if customtkinter.get_appearance_mode() == 'Light': #if it was previously changed to light mode in the same session and is currently light mode, keep the toggle switch at light mode
        dark_mode.select()
    heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30)) #creates the heading of the page as a label
    heading.place(x=230,y=10) #places the heading label

    textbox_TWITTER_ACCESS_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Key") #create the textboxes for the various account credentials and places them
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

    post = customtkinter.CTkButton(master=frame_2, command=go_post, text='Schedule Post') #creates the button to go back to posting page
    post.place(x=450,y=600)

def go_post(): #this is every other line of code in this file (excluding library imports), but the code doesnt work without it

    def convert_number_to_date(number): #function that converts time input into a usable string
        date_string = datetime.strptime(number, '%d%m%Y').strftime('%d %B %Y')
        return date_string

    def youtubecheck(): #function that checks if the youtube box is ticked, is empty since we don't use it but is needed to create the checkbox
        pass

    def twittercheck(): #function that checks if the twitter box is ticked, is empty since we don't use it but is needed to create the checkbox
        pass

    def tiktokcheck(): #function that checks if the tiktok box is ticked, is empty since we don't use it but is needed to create the checkbox
        pass

    def instacheck(): #function that checks if the instagram box is ticked, is empty since we don't use it but is needed to create the checkbox
        pass

    titleadded = False  #placeholder variable, only there so that title can be displayed once entered
    def titleadd():
        global titleadded
        global video_title
        if titleadded == True: #if a title has been previously added, remove it
            destroy_title = lambda: title.destroy()
            destroy_title()
        title_name = title_entry.get() #assign the title that has been entered to variable
        video_title = title_name
        global title
        title=customtkinter.CTkLabel(app, text=f'Title: {title_name}', font=('Helvetica', 15)) #create the label for the title
        title.place(x=70,y=300) #place the label
        titleadded = True

    captionadded = False #placeholder variable, only there so that caption can be displayed once entered
    def descriptionadd():
        global captionadded
        global video_caption
        if captionadded == True: #if a caption has been previously added, remove it
            destroy_caption = lambda: caption.destroy()
            destroy_caption()
        caption_name = caption_entry.get("1.0", 'end-1c') #assign the caption that has been entered to variable
        video_caption = caption_name
        global caption
        caption=customtkinter.CTkLabel(app, text=f'Caption: {caption_name}', font=('Helvetica', 15)) #create the label for the caption
        caption.place(x=70,y=430) #place the label
        captionadded = True
        
    timeadded = False #placeholder variable, only there so that time can be displayed once entered
    def timeadd():
        global upload_time
        time_str = time_entry.get() #assign the time that has been entered to variable
        if not time_str.isdigit() or len(time_str) != 4: #if the time does not fit the needed format of HHMM, reject it
            raise ValueError("Input should be a 4-digit time string in the format 'HHMM'")
        else:
            hour = int(time_str[:2]) #formats the time input into a usable string
            minute = int(time_str[2:])
            formatted_time = f"{hour}:{minute:02d}"

        global timeadded
        if timeadded == True: #if a time has been previously added, remove it
            destroy_time = lambda: timevar.destroy()
            destroy_time()
        formatted_time = f"{hour}:{minute:02d}"
        upload_time = formatted_time 
        global timevar
        timevar=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15)) #create the label for the time
        timevar.place(x=70,y=330) #place the label
        timeadded = True

    dateadded = False #placeholder variable, only there so that date can be displayed once entered
    def dateadd():
        global upload_date
        day = date_entry.get()[:2] #assign the date that has been entered to variables based on day, month and year
        month = date_entry.get()[2:4]
        year = date_entry.get()[4:]
        upload_date = f"{day}/{month}/{year}" #create a usable string and assign it to variable
        global dateadded
        if dateadded == True: #if a date has been previously added, remove it
            destroy_date = lambda: date.destroy()
            destroy_date()
        global date
        date=customtkinter.CTkLabel(app, text=f'Date: {upload_date}', font=('Helvetica', 15)) #create the date for the time
        date.place(x=70,y=360) #place the label
        dateadded = True

    fileadded = False #placeholder variable, only there so that file path can be displayed once entered
    def choose_file():
        file_path = str(fd.askopenfile())[25:-28] #asks user to create a 
        print(file_path)
        if len(file_path) > 25: #if the file path exceeds 25 characters, use the next line
            file_path = file_path[:25] + "\n" + file_path[25:]
        global fileadded
        if fileadded == True: #if a file has been previously added, remove it
            destroy_file = lambda: file.destroy()
            destroy_file()
        global file
        file=customtkinter.CTkLabel(app, text=f'File: {file_path}', font=('Helvetica', 15)) #create the date for the file path
        file.place(x=70,y=390) #place the label
        fileadded = True

    def post(): #function to check if the set time has passed, and then post on various platforms
        global upload_date
        global upload_time
        date_time_str = str(upload_date) + " " + str(upload_time)
        end_time = time.strptime(date_time_str, "%d/%m/%Y %H:%M")
        while True:
            current_time = time.localtime()
            if current_time >= end_time:
                if youtubecb.get(): #posts video on youtube
                    '''
                    Start of Jonathan's Code
                    '''
                    def create_service(client_secret_file, api_name, api_version, *scopes, prefix=''): #function to create a service for the youtube api
                        CLIENT_SECRET_FILE = client_secret_file #assign the client secret file to a variable
                        API_SERVICE_NAME = api_name #assign the api name to a variable
                        API_VERSION = api_version #assign the api version to a variable
                        SCOPES = [scope for scope in scopes[0]] #assign the scopes to a variable
                        
                        creds = None #create a variable for the credentials
                        working_dir = os.getcwd() #get the current working directory
                        token_dir = 'token files' #create a variable for the token directory
                        token_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.json' #create a variable for the token file

                        ### Check if token dir exists first, if not, create the folder
                        if not os.path.exists(os.path.join(working_dir, token_dir)): #if the token directory does not exist, create it
                            os.mkdir(os.path.join(working_dir, token_dir)) #create the token directory

                        if os.path.exists(os.path.join(working_dir, token_dir, token_file)): #if the token file exists, load it
                            creds = Credentials.from_authorized_user_file(os.path.join(working_dir, token_dir, token_file), SCOPES) #load the token file
                            # with open(os.path.join(working_dir, token_dir, token_file), 'rb') as token:
                            #   cred = pickle.load(token)

                        if not creds or not creds.valid: #if the credentials are not valid, refresh them
                            if creds and creds.expired and creds.refresh_token: #if the credentials are expired, refresh them
                                creds.refresh(Request())
                            else:
                                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES) #if the credentials are not valid, create them
                                creds = flow.run_local_server(port=0) #create the credentials

                            with open(os.path.join(working_dir, token_dir, token_file), 'w') as token: #save the credentials
                                token.write(creds.to_json()) #save the credentials

                        try:
                            service = build(API_SERVICE_NAME, API_VERSION, credentials=creds, static_discovery=False) #create the service
                            print(API_SERVICE_NAME, API_VERSION, 'service created successfully') #print a message to show that the service has been created
                            return service #return the service
                        except Exception as e: #handle any errors
                            print(e) #print the error
                            print(f'Failed to create service instance for {API_SERVICE_NAME}') #print a message to show that the service has not been created
                            os.remove(os.path.join(working_dir, token_dir, token_file)) #remove the token file
                            return None #return None

                    def video_categories(): #function to get the video categories
                        video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()    #get the video categories
                        df = pd.DataFrame(video_categories.get('items'))                                                #display information as a table
                        return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)                 #Return everything in a single view

                    API_NAME = 'youtube'                                                                                #API used
                    API_VERSION = 'v3'                                                                                  #Version
                    SCOPES = ['https://www.googleapis.com/auth/youtube']                                                #Permission for anything youtuve related
                    client_file = 'client-secret.json'                                                                  #Client secret file
                    service = create_service(client_file, API_NAME, API_VERSION, SCOPES)                                #Create service

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
                        part='snippet,status',                                                                          #Parts of video
                        body=request_body,                                                                              #Body of video
                        media_body=media_file                                                                           #Media file
                    ).execute()                                                                                         #Execute
                    uploaded_video_id = response_video_upload.get('id')                                                 #Get video id

                    response_thumbnail_upload = service.thumbnails().set(                                               #Upload video thumbnail
                        videoId=uploaded_video_id,                                                                      #Uses video id to assign thumbnail
                        media_body=MediaFileUpload('thumbnail.png')                                                     #thumbnail being used
                    ).execute()                                                                                         #Execute



                    video_id = uploaded_video_id                                                                        #Video id
                    counter = 0                                                                                         #Counter
                    response_update_video = service.videos().list(id=video_id, part='status').execute()                 #make api get video status
                    update_video_body = response_update_video['items'][0]                                               #update video body

                    while 10 > counter:                                                                                 #Checks if the video is done processing before updating status to public
                        if update_video_body['status']['uploadStatus'] == 'processed':                                  #Checks if the video is done processing
                            update_video_body['status']['privacyStatus'] = 'public'                                     #Sets the video to public
                            service.videos().update(                                                                    #Updates the video
                                part='status',                                                                          #Part of video
                                body=update_video_body                                                                  #Body of video
                            ).execute()
                            print('Video {0} privacy status is updated to "{1}"'.format(update_video_body['id'], update_video_body['status']['privacyStatus'])) #Prints the video id and privacy status
                            break

                        time.sleep(10)                                                                                 #Checks again every period of time
                        response_update_video = service.videos().list(id=video_id, part='status').execute()            #make api get video status
                        update_video_body = response_update_video['items'][0]                                          #update video body
                        counter += 1                                                                                   #increment counter
                        '''
                        End of Jonathan's code
                        '''                                                                                   #Checks again every period of time 
                if twittercb.get(): #posts video on twitter
                        client = tweepy.Client(access_token=TWITTER_ACCESS_KEY, #create a client that needs 4 API credentials
                                access_token_secret=TWITTER_ACCESS_SECRET,
                                consumer_key=TWITTER_CONSUMER_KEY,
                                consumer_secret=TWITTER_CONSUMER_SECRET)
                        client.create_tweet(text=video_title,media_ids=file_path) #post a tweet, with the title and video
                if instacb.get(): #posts video on instagram
                    '''
                    Start of Shrinithi's Code
                    '''
                    # Create a new instance of the Edge driver
                    driver = webdriver.Edge()

                    # Navigate to Instagram website
                    driver.get("https://www.instagram.com/")                             
                    time.sleep(10) #wait 10 seconds for page to load

                    # Press the tab key 2 times
                    for i in range(2):
                        pyautogui.press('tab') #press tab to navigate to email field

                    pyautogui.typewrite(INSTAGRAM_EMAIL) #type in email
                    pyautogui.press('tab') #press tab
                    pyautogui.typewrite(INSTAGRAM_PASSWORD) #type in password
                    pyautogui.press('enter') #press enter to login

                    time.sleep(10) #wait 10 seconds for page to load
                    # press the tab key 8 times to navigate to the create post button
                    for i in range(8):
                        pyautogui.press('tab')
                    time.sleep(2)
                    pyautogui.press('enter') #press enter to create post
                    time.sleep(10)


                    # Find the file input element and send the file path
                    pyautogui.press('tab') #press tab to navigate to file input element
                    time.sleep(2)
                    pyautogui.press('enter') #press enter to upload video
                    time.sleep(2)
                    pyautogui.hotkey('command', 'shift', 'g') #open the go to folder window
                    time.sleep(2)
                    pyautogui.typewrite(file_path) #type in the file path
                    time.sleep(2)
                    pyautogui.press('enter') #press enter to open the file
                    time.sleep(2)
                    for i in range(2): #press tab 2 times to navigate to the next button
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        time.sleep(2)
                    for i in range(5): #press tab 5 times to navigate to the caption field
                        pyautogui.press('tab')
                    pyautogui.typewrite(video_caption) #type in the caption
                    pyautogui.hotkey('shift', 'tab')   #press shift tab to navigate to the next button
                    pyautogui.hotkey('shift', 'tab')  #press shift tab to navigate to the next button
                    pyautogui.press('enter') #press enter to post the video

                    time.sleep(15) #wait 15 seconds for page to load
                    '''
                    End of Shrinithi's Code
                    '''
                if tiktokcb.get(): #posts video on tiktok
                    # Create a new instance of the Edge driver
                    driver = webdriver.Edge()

                    # Navigate to TikTok website
                    driver.get("https://www.tiktok.com/")
                    time.sleep(2)
                    # Click on the login button
                    login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
                    login_button.click()

                    time.sleep(1)
                    for i in range(3): # navigate to the login page
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    for i in range(2): #logs into the account
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    for i in range(3):
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    pyautogui.typewrite(TIKTOK_EMAIL)
                    pyautogui.press('tab')
                    pyautogui.typewrite(TIKTOK_PASSWORD)
                    pyautogui.press('enter')

                    time.sleep(5)

                    for i in range(8): #enters video information and posts the video
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
                    for i in range(33): #33 looks like a lot, but its intentional
                        pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(10)
                time.sleep(60) #wait for the next minute if the time has not come
                break

    def go_settings():
        def dark_mode_toggle():
            if dark_mode.get(): #set the app to light mode if indicated, if not stick with dark mode
                customtkinter.set_appearance_mode("light")
            else: 
                customtkinter.set_appearance_mode("dark")

        def updatekeys(): #function to update account information in the file
            TWITTER_ACCESS_KEY = textbox_TWITTER_ACCESS_KEY.get() #assigns the information in the textbox to a corresponding variable
            TWITTER_ACCESS_SECRET = textbox_TWITTER_ACCESS_SECRET.get() #same for twitter access secret
            TWITTER_CONSUMER_KEY = textbox_TWITTER_CONSUMER_KEY.get() #same for twitter consumer key
            TWITTER_CONSUMER_SECRET = textbox_TWITTER_ACCESS_SECRET.get() #same for twitter consumer secret
            TIKTOK_EMAIL = textbox_TIKTOK_EMAIL.get() #same for tiktok email
            TIKTOK_PASSWORD = textbox_TIKTOK_PASSWORD.get() #same for tiktok password
            INSTAGRAM_EMAIL = textbox_INSTAGRAM_EMAIL.get() #same for instagram email
            INSTAGRAM_PASSWORD = textbox_INSTAGRAM_PASSWORD.get() #same for instagram password
            all_info = [
                TWITTER_ACCESS_KEY,
                TWITTER_ACCESS_SECRET,
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET,
                TIKTOK_EMAIL,
                TIKTOK_PASSWORD,
                INSTAGRAM_EMAIL,
                INSTAGRAM_PASSWORD
            ] #creates a list of all the information
            key = Fernet.generate_key() #key generation, generates new keys each time
            fernet = Fernet(key) #cast key to fernet type
            
            with open('textinfo.txt','w') as f: #create txt file if it doesnt exist, and write to key
                f.write(str(key)[2:-1] + '\n')
                for i in all_info:
                    encoded = fernet.encrypt(i.encode()) #encodes every line
                    f.write(str(encoded)[2:-1] + '\n')
                f.close()
        frame_1.destroy() #removes the previous page frame
        global frame_2
        frame_2 = customtkinter.CTkFrame(master=app) #creates a new page frame
        frame_2.pack(pady=20, padx=60, fill="both", expand=True)
        dark_mode = customtkinter.CTkSwitch(master=frame_2, command=dark_mode_toggle, text='Light Mode') #creates a toggle switch for the dark/light mdoe
        dark_mode.place(x=70,y=100)
        if customtkinter.get_appearance_mode() == 'Light': #if it was previously changed to light mode in the same session and is currently light mode, keep the toggle switch at light mode
            dark_mode.select()
        heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30)) #creates the heading of the page as a label
        heading.place(x=230,y=10) #places the heading label

        textbox_TWITTER_ACCESS_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Key") #create the textboxes for the various account credentials and places them
        textbox_TWITTER_ACCESS_KEY.place(x=70,y=140)
        textbox_TWITTER_ACCESS_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Access Secret") #same for twitter access secret    
        textbox_TWITTER_ACCESS_SECRET.place(x=70,y=180)
        textbox_TWITTER_CONSUMER_KEY = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Key") #same for twitter consumer key
        textbox_TWITTER_CONSUMER_KEY.place(x=70,y=220)
        textbox_TWITTER_CONSUMER_SECRET = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Twitter Consumer Secret") #same for twitter consumer secret
        textbox_TWITTER_CONSUMER_SECRET.place(x=70,y=260)
        textbox_TIKTOK_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Email") #same for tiktok email
        textbox_TIKTOK_EMAIL.place(x=70,y=300)
        textbox_TIKTOK_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Tiktok Password") #same for tiktok password
        textbox_TIKTOK_PASSWORD.place(x=70,y=340)
        textbox_INSTAGRAM_EMAIL = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Email") #same for instagram email
        textbox_INSTAGRAM_EMAIL.place(x=70,y=380)
        textbox_INSTAGRAM_PASSWORD = customtkinter.CTkEntry(master=frame_2,width=400, placeholder_text="Instagram Password") #same for instagram password
        textbox_INSTAGRAM_PASSWORD.place(x=70,y=420)
        updateinfo = customtkinter.CTkButton(master=frame_2, command=updatekeys, text='Update Information') #creates the button to update the information
        updateinfo.place(x=70,y=540)

        post = customtkinter.CTkButton(master=frame_2, command=go_post, text='Schedule Post') #creates the button to go back to posting page
        post.place(x=450,y=600)

    frame_2.destroy() # removes the settings page
    frame_1 = customtkinter.CTkFrame(master=app) #creates the page frame for the posting page
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title") #creates various labels and their respective textboxes and buttons
    title_entry.place(x=300,y=70)
    title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title') #creates the button to add the title
    title_confirm.place(x=300,y=110)
    caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200) #creates the textbox for the description
    caption_entry.place(x=300,y=160)
    caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description') #creates the button to add the description
    caption_confirm.place(x=300,y=370)
    time_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="HHMM") #creates the textbox for the time
    time_entry.place(x=300,y=420)
    time_confirm = customtkinter.CTkButton(master=frame_1, command=timeadd, text='Add Time') #creates the button to add the time
    time_confirm.place(x=300,y=460)
    date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY") #creates the textbox for the date
    date_entry.place(x=300,y=510)
    date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date') #creates the button to add the date
    date_confirm.place(x=300,y=550)
    file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select Video File') #creates the button to select the video file
    file_select.place(x=300,y=590)
    post_button = customtkinter.CTkButton(master=frame_1, command=post, text='Schedule!') #creates the button to schedule the post
    post_button.place(x=300,y=630)
    heading = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post', font=('Helvetica', 30)) #creates the heading label
    heading.place(x=230,y=10)

    youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube', font=('Helvetica', 20)) #creates various checkboxes and their respective platform names
    youtubecb.place(x=70,y=70)
    twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter', font=('Helvetica', 20)) #same for twitter
    twittercb.place(x=70,y=120)
    tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok', font=('Helvetica', 20)) #same for tiktok
    tiktokcb.place(x=70,y=170)
    instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram', font=('Helvetica', 20)) #same for instagram
    instacb.place(x=70,y=220)

    settings = customtkinter.CTkButton(master=frame_1, command=go_settings, text='Settings') #creates the button to go to the settings page
    settings.place(x=450,y=600)

    app.mainloop() #runs the app

frame_1 = customtkinter.CTkFrame(master=app) #creates the page frame for the posting page
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title") #creates 
title_entry.place(x=300,y=70)
title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title') #creates the button to add the title
title_confirm.place(x=300,y=110)
caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200) #creates the textbox for the description
caption_entry.place(x=300,y=160)
caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description') #creates the button to add the description
caption_confirm.place(x=300,y=370)
time_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="HHMM") #creates the textbox for the time
time_entry.place(x=300,y=420)
time_confirm = customtkinter.CTkButton(master=frame_1, command=timeadd, text='Add Time')  #creates the button to add the time
time_confirm.place(x=300,y=460)
date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY") #creates the textbox for the date
date_entry.place(x=300,y=510)
date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date') #creates the button to add the date
date_confirm.place(x=300,y=550)
file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select Video File')
file_select.place(x=300,y=590)
post_button = customtkinter.CTkButton(master=frame_1, command=post, text='Schedule!')
post_button.place(x=300,y=630)
heading = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post', font=('Helvetica', 30))
heading.place(x=230,y=10)

youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube', font=('Helvetica', 20)) #creates various checkboxes and their respective platform names
youtubecb.place(x=70,y=70)
twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter', font=('Helvetica', 20))
twittercb.place(x=70,y=120)
tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok', font=('Helvetica', 20))
tiktokcb.place(x=70,y=170)
instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram', font=('Helvetica', 20))
instacb.place(x=70,y=220)

settings = customtkinter.CTkButton(master=frame_1, command=go_settings, text='Settings') #creates the button to go to the settings page
settings.place(x=450,y=600)

app.mainloop() #runs the app