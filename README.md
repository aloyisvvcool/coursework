# Sociable

###### Sociable is a Python program that allows you to create and schedule social media posts on Twitter, TikTok, Instagram, and YouTube

## Prerequisites

#### This program requires Python 3.0 or higher to be installed on your MacOS machine. It also requires the following Python libraries to be installed

- tkinter
- customtkinter
- datetime
- selenium
- pyautogui
- time
- tweepy
- pandas
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

#### You can install these libraries using pip. To do so, open a terminal window and run the following command

```bash
pip3 install --force --upgrade tk customtkinter datetime selenium pyautogui tweepy google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```

#### In addition, if you plan to use the YouTube functionality, you will need to

1. Sign in to Google Cloud and use the free trial (even if the trial runs out, you can still use it).
2. Create a new project.
3. Go to API's and services.
4. Go to "libraries" and enable the YouTube library for that project.
5. Go to credential and click "create credentials."
6. Select "Oauth client ID."
7. Choose "desktop app" as the application type.
8. Click create and in the credentials tab, click the edit button for that credential.
9. Click the "download JSON" button.
10. Save the downloaded JSON file to the 'Socialable' directory

#### Note: The program uses Selenium and a web driver to interact with the social media platforms. Make sure you have the appropriate web drivers installed on your machine and update the file path for the TikTok post to run the program successfully

##### This program uses also Youtube API directly from the channel/accounts's API, thus following the steps to save the required JSON file to the correctly location is important if you are looking to to use this for Youtube

###### Alternatively, you can follow the steps from the ***[official documentation](https://developers.google.com/youtube/v3/quickstart/python)*** if you are still unclear on what you have to do

## How to Run the Program

To run the program, navigate to the directory where the code is saved in a terminal window and run the following command:

```bash
python3 app.py
```

## Usage

#### This program is a graphical user interface (GUI) that allows you to add a title, caption, date, and time to a social media post on Twitter, TikTok, Instagram, or YouTube. To use the program, follow these steps

1. Run the program using the instructions above.
2. Select the checkboxes for the social media platforms you want to post on.
3. Enter a title for your post in the "Title" field.
4. Enter a caption for your post in the "Caption" field.
5. Enter the date and time you want to post your message in the "Date" and "Time" fields. The date should be in the format "DDMMYYYY" and the time should be in the format "HHMM".
6. Click the "Add Title", "Add Description", "Add Time", and "Add Date" buttons to add your post details to the GUI.
7. If you are uploading a video to Youtube, a thumbnail of size 1280x720 is required, else you can skip this step.
8. Once you have added all your post details, click the "Post" button to post your message on the selected social media platforms.

###### This project does not have a license
