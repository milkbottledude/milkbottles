from zenbumada import SomeHololiveMembers
import pandas as pd
from apiclient.discovery import build

def getYT():
    youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')

    ch_request = youtube.channels().list(part='statistics', id='UC-hM6YJuNYVAmUWxeIr9FeA')
    ch_response = ch_request.execute()

    sub = ch_response['items'][0]['statistics']['subscriberCount']
    vid = ch_response['items'][0]['statistics']['videoCount']
    views = ch_response['items'][0]['statistics']['viewCount']


# print('Total subs: ', sub)
# print('Total no. of videos: ', vid)
# print('Total views: ', views)

def getyt(name):
    youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')
    request = youtube.search().list(q=name, type='channel', part='id', maxResults=1)
    response = request.execute()
    channel_id = response['items'][0]['id']['channelId']
     # Use the channel ID to get the channel statistics
    request = youtube.channels().list(part='statistics', id=channel_id)
    response = request.execute()
    
    viewCount = response['items'][0]['statistics']['viewCount']
    subscriberCount = response['items'][0]['statistics']['subscriberCount']
    videoCount = response['items'][0]['statistics']['videoCount']



