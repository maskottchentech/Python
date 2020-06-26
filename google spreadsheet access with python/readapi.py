import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)
client = gspread.authorize(credentials)
sheet = client.open("xyz").sheet1
data = sheet.get_all_records()
print(data)
sheet.update_cell(5,4,"abcd")
