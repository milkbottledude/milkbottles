import pandas as pd
from apiclient.discovery import build
gsheetid = '1fIOVbvK4ox2PZSt1hVOVszIZ-PrrHARPxF-U60iS2CQ'
# sheet_name = "min'na"
# gsheet_url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
# df = pd.read_csv(gsheet_url)
youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')

def open_gsheet(sheetname):
    gsheet_url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheetname}'
    df0 = pd.read_csv(gsheet_url)
    return df0

def pretty_form(messyshi):
    messy = float('%.3g' % int(messyshi))
    if messy > 999999999:
        return f'{messy/1000000000}b' 
    elif messy > 999999:
        return f'{messy/1000000}m'
    elif messy > 999:
        return f'{messy/1000}k'


def getyt(name):
    youtube = build('youtube', 'v3', developerKey='AIzaSyCxImnrniRROJjrunMMUEIKGq8clMbt-uU')
    request = youtube.search().list(q=name, type='channel', part='id', maxResults=1)
    response = request.execute()
    channel_id = response['items'][0]['id']['channelId']
     # Use the channel ID to get the channel statistics
    request = youtube.channels().list(part='statistics', id=channel_id)
    response = request.execute()
    
    viewCount = response['items'][0]['statistics']['viewCount']
    # subscriberCount = response['items'][0]['statistics']['subscriberCount']
    # videoCount = response['items'][0]['statistics']['videoCount']

# names = df.loc[:, 'Name']
# for name in names:
#     getyt(name)

# del df['View Count']
# df.insert(6, 'View Count', view_count)

# getyt('hoshou marine')
# print(subCount)
# print(channelid)
from df_to_gsheet import df_to_gsheet_func
def save(sheetindex, dafa):
    df_to_gsheet_func(sheetindex, dafa)

# df2 = df.groupby('Generation', sort=False)['View Count'].sum()


df0 = open_gsheet('by_gen')

viewCavg = []
for x in range(15):
    avg = df0.loc[x,'ViewCsum aka'] / df0.loc[x, 'Member Count']
    viewCavg.append(avg)

df0.insert(3, 'viewCavg', viewCavg)
print(df0)
save(2, df0)