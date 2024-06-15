import pandas as pd
from apiclient.discovery import build
gsheetid = '1fIOVbvK4ox2PZSt1hVOVszIZ-PrrHARPxF-U60iS2CQ'
sheet_name = 'holomem'
gsheet_url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(gsheet_url)

def getsub():
    youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')

    ch_request = youtube.channels().list(part='statistics', id='UC-hM6YJuNYVAmUWxeIr9FeA')
    ch_response = ch_request.execute()

    sub = ch_response['items'][0]['statistics']['subscriberCount']

def getview(ID):
    youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')
    ch_request = youtube.channels().list(part='statistics', id=ID)
    ch_response = ch_request.execute()
    views = ch_response['items'][0]['statistics']['viewCount']
    return views

def standard_form(messyshi):
    messy = float('%.3g' % messyshi)
    if messy > 1000000000:
        return f'{messy/1000000000}b' 
    elif messy > 1000000:
        return f'{messy/1000000}m'
    elif messy > 1000:
        return f'{messy/1000}k'
    
ids = df.loc[:, 'Channel id']


sube = df.loc[:, 'Sub Count']
subp = []
for sub in sube:
    subp.append(standard_form(sub))

df.insert(6, 'subC sf', subp)

viewe = df.loc[:, 'View Count']
viewp = []
for view in viewe:
    viewp.append(standard_form(view))

df.insert(8, 'view sf', viewp)




from df_to_gsheet import df_to_gsheet_func
def save():
    df_to_gsheet_func(0, df)
print(save())