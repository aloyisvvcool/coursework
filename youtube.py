import datetime


import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

import time
from googleapiclient.http import MediaFileUpload
import pandas as pd


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
        'title': 'Hello?????',                                                                   #Insert title of video
        'description': 'wassup my guys this is test #2',                                                       #Insert video desciption
        'categoryId': '26',                                                              #Insert category id
        'tags': ['youtube api']                                                                            #Insert video tags
    },
    'status': {
        'privacyStatus': 'private',                                                                 #Status privacy
        'publishedAt': upload_time,                                                                   #Post the video
        'selfDeclaredMadeForKids': False                                                            #Kids?
    },
    'notifySubscribers': False                                                                      #Will the video notify subscibers
}

video_file = 'videotest.mp4'                                                                        #Finds video file (mp4)
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
    counter += 1                                                                                    #Checks again every period of time 
'''

'''
