import json, gspread, datetime
from flask import request
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

######Post to Test Sheet
# def writeToLog(site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note):
#   sh = gc.open("TEST Session Tracker").sheet1
#   date=str(datetime.datetime.now()).split(' ')[0]
#   print date
#   values=[date,site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note]
#   print 'values in sheet.py ',values
#   sh.append_row(values)
  
######Post to prod Sheet
def writeToLog(site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note):
  sh = gc.open_by_key('1bRKYdXR6-Q3iRHZfOU5ycIzNaXCO3gdng2PkZwtvmM4').sheet1 #ID of log sheet
  #sh = gc.open("Bridging Berkeley Session Tracker").sheet1
  date=str(datetime.datetime.now()).split(' ')[0]
  print date
  values=[date,site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note]
  print 'values in sheet.py ',values
  sh.append_row(values)
  

# def pull_data():
#     sh = gc.open("Bridging Berkeley Session Tracker")
#     worksheet = sh.sheet1
#     students_at_site=[]
#     for row in worksheet.get_all_values():
#         students_at_site.append(row)
#     print 'reading from sheet==== ',students_at_site

# pull_data()

def pull_students():
    sh = gc.open_by_key('16u543i4DobE7FW4mdkHNAD1PYvuxwRUca2NmmqZjw84').sheet1 #id of student list sheet
    students_list=[]
    for row in sh.col_values(4):
          if row!='' and row !='FullName':
            students_list.append(row)

    return students_list
    #return students_list
    #students= pull_students('Berkeley') 
    
#pull_students()
