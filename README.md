###### To view this page in Markdown, open [https://echo.notable.app/19c62a8b871ed5d82b8a462c2a8aed581d531fd0bea45751f2dd8a8559d63a74](https://echo.notable.app/19c62a8b871ed5d82b8a462c2a8aed581d531fd0bea45751f2dd8a8559d63a74) in your preferred browser

2023 Computing+ Coursework: Sociable - A Social Media Posting App
By: Aloysius (S4-01), Shrinithi (S4-01), Jonathan (S4-07)

---

# Sociable

###### Sociable is a Python program that allows you to create and schedule social media posts on Twitter, TikTok, Instagram, and YouTube - currently streamlined for MacOS only

## Simplified Video

Uploading comp coursework.mp4…

## Prerequisites

#### This program requires [Microsoft Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ) to be installed at /Applications/ on your MacOS system

###### Microsoft Edge (Public Release - Non Beta Version)

#### This program requires Python 3.0 or higher to be installed on your MacOS machine. It also requires the following Python libraries (with their respective version numbers) to be installed

| Package Name             | Version      |
|--------------------------|--------------|
| tk                       | 0.1.0        |
| customtkinter            | 5.1.2        |
| DateTime                 | 5.0          |
| selenium                 | 4.8.2        |
| PyAutoGUI                | 0.9.53       |
| tweepy                   | 4.12.1       |
| pandas                   | 1.5.3        |
| google-auth              | 2.16.1       |
| google-auth-oauthlib     | 1.0.0        |
| google-auth-httplib2     | 0.1.0        |
| google-api-python-client | 2.78.0       |

#### You can install these libraries using pip. To do so, open a terminal window and run the following command

```bash
pip3 install --force --upgrade tk==0.1.0 customtkinter==5.1.2 DateTime==5.0 selenium==4.8.2 PyAutoGUI==0.9.53 tweepy==4.12.1 pandas==1.5.3 google-auth==2.16.1 google-auth-oauthlib==1.0.0 google-auth-httplib2==0.1.0 google-api-python-client==2.78.0
```

#### To check your version numbers of the list of packages, you can open a terminal window and run the following command

```bash
pip3 show tk==0.1.0 customtkinter==5.1.2 DateTime==5.0 selenium==4.8.2 PyAutoGUI==0.9.53 tweepy==4.12.1 pandas==1.5.3 google-auth==2.16.1 google-auth-oauthlib==1.0.0 google-auth-httplib2==0.1.0 google-api-python-client==2.78.0
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

#### The program uses Selenium and a web driver to interact with the social media platforms. Make sure you have the appropriate web drivers installed on your machine and update the file path for the TikTok post to run the program successfully

#### This program also uses Youtube API directly from the channel/accounts's API, thus following the steps to save the required JSON file to the correctly location is important if you are looking to to use this for Youtube

###### Alternatively, you can follow the steps from the ***[official documentation](https://developers.google.com/youtube/v3/quickstart/python)*** if you are still unclear on what you have to do

## How to Run the Program

To run the program, navigate to the directory where the code is saved in a terminal window and run the following command:

```bash
python3 app.py
```

###### Alternatively, you can run ***app.py*** on IDLE

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

#### The App might appear to be frozen until the selected media is posted - please do not quit the app unless it is frozen due to another issue

###### This project does not require a license
