import pandas as pd
gsheetid = '1fIOVbvK4ox2PZSt1hVOVszIZ-PrrHARPxF-U60iS2CQ'
sheet_name = 'holomem'
gsheet_url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(gsheet_url)



print(df)
