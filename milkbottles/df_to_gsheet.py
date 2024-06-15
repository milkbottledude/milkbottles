gsheet_id = 'https://docs.google.com/spreadsheets/d/1fIOVbvK4ox2PZSt1hVOVszIZ-PrrHARPxF-U60iS2CQ/edit#gid=0'
# import sys, subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])

import gspread
from typing_extensions import Literal

def df_to_gsheet_func(worksheet_index, df):
    import gspread
    from typing_extensions import Literal

    sheet_credential = gspread.service_account('google_credentials.json')
    spreadsheet = sheet_credential.open_by_url(gsheet_id)
    print(spreadsheet.title)

    worksheet = spreadsheet.get_worksheet(worksheet_index)
    # importing entire df to google sheets
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return 'df saved as gsheet'



def insertColumn(num_of_cols, capsletter):
    worksheet.insert_cols(str(int(num_of_cols) * 'a'), ord(capsletter) - 64)

# worksheet.update('C1', [['abc', 'ghi'], ['def']])
# # read data after update
# update_data = worksheet.get_all_values()
# for valu in update_data:
#     print(valu)

# importing entire df to google sheets
# from pandasintro import df
# worksheet.update([df.columns.values.tolist()] + df.values.tolist())
