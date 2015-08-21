import json, gspread
from flask import request
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)


sh = gc.open("Master Log")
worksheet = sh.sheet1

for row in worksheet.get_all_values():
    print row
    # do something. row is a list; try printing row, row[0], etc.