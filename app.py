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
    print(f"{hour}:{minute:02d} {am_pm}")


def choose_file():
    print(str(fd.askopenfile())[25:-28])

def descriptionadd():
    print(caption_entry.get("1.0", 'end-1c'))

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

#fix this lol

app.tabview = customtkinter.CTkTabview(app, width=720, height=720)
app.tabview.place(x=0 , y=0)
app.tabview.add("CTkTabview")
app.tabview.add("Tab 2")
app.tabview.add("Tab 3")
app.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
app.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
app.label_tab_2 = customtkinter.CTkLabel(app.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
app.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text='New Post')
label_1.place(x=200,y=10)

youtubecb = customtkinter.CTkCheckBox(master=frame_1, command=youtubecheck, text='Youtube')
youtubecb.place(x=10,y=50)

twittercb = customtkinter.CTkCheckBox(master=frame_1, command=twittercheck, text='Twitter')
twittercb.place(x=10,y=100)

tiktokcb = customtkinter.CTkCheckBox(master=frame_1, command=tiktokcheck, text='Tiktok')
tiktokcb.place(x=10,y=150)

instacb = customtkinter.CTkCheckBox(master=frame_1, command=instacheck, text='Instagram')
instacb.place(x=10,y=200)

title_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title")
title_entry.place(x=300,y=50)
title_confirm = customtkinter.CTkButton(master=frame_1, command=titleadd, text='Choose Title')
title_confirm.place(x=300,y=90)

caption_entry = customtkinter.CTkTextbox(master=frame_1, height=200)
caption_entry.place(x=300,y=140)
caption_confirm = customtkinter.CTkButton(master=frame_1, command=descriptionadd, text='Choose Description')
caption_confirm.place(x=300,y=350)

time_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="HHMM")
time_entry.place(x=300,y=400)
time_confirm = customtkinter.CTkButton(master=frame_1, command=timeadd, text='Add Time')
time_confirm.place(x=300,y=440)

date_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="DDMMYYYY")
date_entry.place(x=300,y=490)
date_confirm = customtkinter.CTkButton(master=frame_1, command=dateadd, text='Add Date')
date_confirm.place(x=300,y=530)

file_select = customtkinter.CTkButton(master=frame_1, command=choose_file, text='Select Video File')
file_select.place(x=300,y=580)

app.mainloop()
