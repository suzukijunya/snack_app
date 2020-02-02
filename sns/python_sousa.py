import gspred
import json
from oauth2client.service_account import ServiceAcountCredentials

JSON = 'mojiokoshikun-d535686a4032.json'

SPREDSHEET_KEY = '1M--svMok-j20mV3anAnbzNe161ilSrWPi0RzKcyLsps'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

Credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON, scope)
gc = gspread.authorize(credentials)

worksheet = gc.open_by_key(SPREDSHEET_KEY).sheet1
import_value = int(worksheet.acell('A1').value)
export_value = import_value+100
worksheet.update_cell(1,2, export_value)