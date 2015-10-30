import json, gspread, datetime
from flask import request
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)
# print 'JSON KEY============',json_key
# print 'CREDS+++++++++++++',credentials
#submit form into to spreadsheet
def write_to_log(site,mentor,absences,scholar,duration, math_topic, scholar_ranking, mentor_ranking, note):
  sh = gc.open("Bridging Berkeley Session Tracker").sheet1
  date=str(datetime.datetime.now()).split(' ')[0]
  print date
  values=[date,site,mentor,absences,scholar,duration,math_topic, scholar_ranking, mentor_ranking, note]
  print values
  sh.append_row(values)
  
#write_to_log('test',1,1,1,1,1,1,1,1)


#filter out the students at your desired site location
# def pull_students(site):
#     sh = gc.open("Student_ref")
#     worksheet = sh.sheet1
#     students_at_site=[]

#     for row in worksheet.get_all_values():
#         if row[5].upper()==site.upper():
#             students_at_site.append(row)

#     print students_at_site
#     return students_at_site
#     #students= pull_students('Berkeley') 
