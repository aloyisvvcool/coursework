import tkinter
import customtkinter
from datetime import datetime
from tkinter import filedialog as fd

def convert_number_to_date(number):
    date_string = datetime.strptime(number, '%d%m%Y').strftime('%d %B %Y')
    return date_string
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("720x720")
app.title("APP")

def youtubecheck():
    print(youtubecb.get())

def twittercheck():
    print(twittercb.get())

def tiktokcheck():
    print(tiktokcb.get())

def instacheck():
    print(instacb.get())

def titleadd():
    print(title_entry.get())

def dateadd():
    date_string = datetime.strptime(date_entry.get(), '%d%m%Y').strftime('%d %B %Y')
    print(date_string)

def choose_file():
    print(str(fd.askopenfile()))

def descriptionadd():
    print(caption_entry.getvar())

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post')
label_1.pack(pady=10, padx=10)

youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube')
youtubecb.pack(pady=10, padx=10)

twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter')
twittercb.pack(pady=10, padx=10)

tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok')
tiktokcb.pack(pady=10, padx=10)

instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram')
instacb.pack(pady=10, padx=10)

title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title")
title_entry.pack(pady=10, padx=10)
title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title')
title_confirm.pack(pady=10, padx=10)

caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200)
caption_entry.pack(pady=10, padx=10)
caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description')
caption_confirm.pack(pady=10, padx=10)

date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY")
date_entry.pack(pady=10, padx=10)
date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date')
date_confirm.pack(pady=10, padx=10)

file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select File')
file_select.pack(pady=10, padx=10)

app.mainloop()
