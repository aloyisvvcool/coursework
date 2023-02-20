# Requirements

This program requires Python 3.0 or higher to be installed on your MacOS machine. It also requires the following Python libraries to be installed:

- tkinter
- customtkinter
- datetime
- selenium
- pyautogui
- time
- tweepy
- cryptography

You can install these libraries using pip. To do so, open a terminal window and run the following command:

```bash
  pip3 install --force --upgrade tkinter customtkinter datetime selenium pyautogui time tweepy cryptography

```
# How to Run the Program

To run the program, navigate to the directory where the code is saved in a terminal window and run the following command:

```bash
  python3 app.py
```

# Usage

This program is a graphical user interface (GUI) that allows you to add a title, caption, date, and time to a social media post on Twitter, TikTok, Instagram, or YouTube. To use the program, follow these steps:

1. Run the program using the instructions above.
2. Select the checkboxes for the social media platforms you want to post on.
3. Enter a title for your post in the "Title" field.
4. Enter a caption for your post in the "Caption" field.
5. Enter the date and time you want to post your message in the "Date" and "Time" fields. The date should be in the format "DDMMYYYY" and the time should be in the format "HHMM".
6. Click the "Add Title", "Add Description", "Add Time", and "Add Date" buttons to add your post details to the GUI.
7. Once you have added all your post details, click the "Post" button to post your message on the selected social media platforms.

Note: The program uses Selenium and a web driver to interact with the social media platforms. Make sure you have the appropriate web drivers installed on your machine and update the file path for the TikTok post to run the program successfully.

License

This project does not have a license.