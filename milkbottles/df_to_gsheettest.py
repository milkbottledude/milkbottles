gsheet_id = 'https://docs.google.com/spreadsheets/d/1fIOVbvK4ox2PZSt1hVOVszIZ-PrrHARPxF-U60iS2CQ/edit#gid=0'
# import sys, subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])

import gspread
from typing_extensions import Literal

sheet_credential = gspread.service_account('google_credentials.json')
spreadsheet = sheet_credential.open_by_url(gsheet_id)
print(spreadsheet.title)

worksheet = spreadsheet.get_worksheet(1)
#some sorcery shi for inserting column, there will be error msg but it works trust
def insertColumn(num_of_cols, capsletter):
    worksheet.insert_cols(str(int(num_of_cols) * 'a'), ord(capsletter) - 64)
worksheet.update('B1', [['Channel Name']])