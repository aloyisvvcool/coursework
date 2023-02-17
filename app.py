import tkinter
import customtkinter
from datetime import datetime
from tkinter import filedialog as fd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import tweepy

EMAIL = 'plsgivea1@gmail.com'
TT_PASSWORD = "compa1orcry!"
ACCESS_KEY = 'test_access_kEy'
ACCESS_SECRET = 'test_access_secRET'
CONSUMER_KEY = 'test_consumer_KEy'
CONSUMER_SECRET = 'tEST_Consumer_secret'
file_path = None #initialised just so tiktok posting can run, should be changed later on
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("720x720")
app.title("APP")

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
    time_str = time_entry.get()
    if not time_str.isdigit() or len(time_str) != 4:
        raise ValueError("Input should be a 4-digit time string in the format 'HHMM'")
    hour = int(time_str[:2])
    minute = int(time_str[2:])
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
    formatted_time = f"{hour}:{minute:02d} {am_pm}"

    global timeadded
    if timeadded == True:
        destroy_time = lambda: time.destroy()
        destroy_time()
    formatted_time = f"{hour}:{minute:02d} {am_pm}"
    global time
    time=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15))
    time.place(x=70,y=330)
    timeadded = True

dateadded = False
def dateadd():
    date_string = datetime.strptime(date_entry.get(), '%d%m%Y').strftime('%d %B %Y')
    print(date_string)
    global dateadded
    if dateadded == True:
        destroy_date = lambda: date.destroy()
        destroy_date()
    global date
    date=customtkinter.CTkLabel(app, text=f'Date: {date_string}', font=('Helvetica', 15))
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
    if youtubecb.get(): #youtube upload code here
        pass
    if twittercb.get(): #twitter upload code here
        client = tweepy.Client(access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET)

    picture = client.media_upload("media1.png") #picture part is optional, remove from line below if not used
    client.create_tweet(text='test',media_ids=picture)
    if tiktokcb.get(): #tiktok upload code here
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

        pyautogui.typewrite(EMAIL)
        pyautogui.press('tab')
        pyautogui.typewrite(TT_PASSWORD)
        pyautogui.press('enter')

        time.sleep(10)

        for i in range(5):
            pyautogui.press('tab')
        pyautogui.press('enter') # go to posting page

        s = driver.find_element(By.XPATH, "//input[@type='Select file']")
        s.send_keys(file_path)

        for i in range(4): # go to caption entry
            pyautogui.press('tab')
        pyautogui.typewrite(caption)
        for i in range(5): # go to post button
            pyautogui.press('tab')
        pyautogui.press('enter') # post
        time.sleep(3) # wait 3 seconds then close window
    if instacb.get(): #instagram upload code here
        pass

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
    dark_mode.place(x=70,y=130)
    if customtkinter.get_appearance_mode() == 'Light':
        dark_mode.select()
    heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30))
    heading.place(x=230,y=10)
    post = customtkinter.CTkButton(master=frame_2, command=go_post, text='Schedule Post')
    post.place(x=450,y=600)

def go_post():
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
        time_str = time_entry.get()
        if not time_str.isdigit() or len(time_str) != 4:
            raise ValueError("Input should be a 4-digit time string in the format 'HHMM'")
        hour = int(time_str[:2])
        minute = int(time_str[2:])
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
        formatted_time = f"{hour}:{minute:02d} {am_pm}"

        global timeadded
        if timeadded == True:
            destroy_time = lambda: time.destroy()
            destroy_time()
        formatted_time = f"{hour}:{minute:02d} {am_pm}"
        global time
        time=customtkinter.CTkLabel(app, text=f'Time: {formatted_time}', font=('Helvetica', 15))
        time.place(x=70,y=330)
        timeadded = True

    dateadded = False
    def dateadd():
        date_string = datetime.strptime(date_entry.get(), '%d%m%Y').strftime('%d %B %Y')
        print(date_string)
        global dateadded
        if dateadded == True:
            destroy_date = lambda: date.destroy()
            destroy_date()
        global date
        date=customtkinter.CTkLabel(app, text=f'Date: {date_string}', font=('Helvetica', 15))
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
        if youtubecb.get(): #youtube upload code here
            pass
        if twittercb.get(): #twitter upload code here
            client = tweepy.Client(access_token=ACCESS_KEY,
                        access_token_secret=ACCESS_SECRET,
                        consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET)

        picture = client.media_upload("media1.png") #picture part is optional, remove from line below if not used
        client.create_tweet(text='test',media_ids=picture)
        if tiktokcb.get(): #tiktok upload code here
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

            pyautogui.typewrite(EMAIL)
            pyautogui.press('tab')
            pyautogui.typewrite(TT_PASSWORD)
            pyautogui.press('enter')

            time.sleep(10)

            for i in range(5):
                pyautogui.press('tab')
            pyautogui.press('enter') # go to posting page

            s = driver.find_element(By.XPATH, "//input[@type='Select file']")
            s.send_keys(file_path)

            for i in range(4): # go to caption entry
                pyautogui.press('tab')
            pyautogui.typewrite(caption)
            for i in range(5): # go to post button
                pyautogui.press('tab')
            pyautogui.press('enter') # post
            time.sleep(3) # wait 3 seconds then close window
        if instacb.get(): #instagram upload code here
            driver = webdriver.Edge()

            # Navigate to Instagram website
            driver.get("https://www.instagram.com/")                             
            time.sleep(5)

            # Press the tab key 2 times
            for i in range(2):
                pyautogui.press('tab')

            pyautogui.typewrite(EMAIL)
            pyautogui.press('tab')
            pyautogui.typewrite(TT_PASSWORD) #insta uses same password
            pyautogui.press('enter')

            time.sleep(10)
            # press the tab key 8 times
            for i in range(8):
                pyautogui.press('tab')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(10)

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
        dark_mode.place(x=70,y=130)
        if customtkinter.get_appearance_mode() == 'Light':
            dark_mode.select()
        heading = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT, text='Settings', font=('Helvetica', 30))
        heading.place(x=230,y=10)
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