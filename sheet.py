import json, gspread
from flask import request
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

def write_to_log():
  sh = gc.open("Master Log")
  worksheet = sh.sheet1
  values=['1','test','me']
  worksheet.append_row(values)
  
write_to_log()

#filter out the students at your desired site location

def pull_students(site):
    sh = gc.open("Student_ref")
    worksheet = sh.sheet1
    students_at_site=[]

    for row in worksheet.get_all_values():
        if row[2].upper()==site.upper():
            students_at_site.append(row)

    return students_at_site
    #students= pull_students('Berkeley') 
