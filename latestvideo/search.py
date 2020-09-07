from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey

class YoutubeBot:
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        ids = [] #stores the video ids
        channelid = "UCiBfuUreTbKvBKtQbb6SIWQ" # change this to your youtube channel id 
        maxResults = 5
        youtube = build('youtube', 'v3', developerKey=apikey)
        request = youtube.search().list(part="snippet",channelId=channelid,maxResults=maxResults,order="date",type="video")
        response = request.execute()
        for item in response['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))
        print(response)
        return ids

        
bot = YoutubeBot()
print(bot.getVids())