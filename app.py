import requests, gspread, os
from flask import Flask, request, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from sheet import *

app = Flask(__name__) 
app.secret_key = 'thisisasecret'

GOOGLE_CLIENT_ID = '834450588178-tmqi729odq8h0vkbik3rk9rm4no4aqgp.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'epOQT9krb6yKrkj7tu74PBEy'
auth = HTTPBasicAuth()

users = {"build": "volunteer"}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')


@app.route('/submitLog',methods=['POST'])
def submitform():
    try:
        site=request.form.get('site')
        mentor=request.form.get('mentor')
        scholar=request.form.get('scholar')
        absence=0
        if request.form.get('absenceCheck'): #absenceCheck returns 'checked' or None
            absence=1
        isDropin=request.form.get('isDropin')
        math_topic=request.form.get('math_topic')
        duration=int(request.form.get('duration'))
        mentor_rank=int(request.form.get('mentor_rank'))
        scholar_rank=int(request.form.get('scholar_rank'))
        note=request.form.get('notes')
        print 'Form Data =====>',site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note
        print 'NOT YET written to log'
        writeToLog(site,mentor,scholar,absence,isDropin,duration, math_topic, mentor_rank,scholar_rank, note)
        print 'SUCCESSFULLY Written to log'
        post_success=True
        message='Thank you for submitting your activity.'
     
        return render_template('index.html',post_success=post_success,message=message)
    except: 
        print 'FAILED'
        post_success=False
        message='Opps! Missing form data. Please fill out all the fields and try again.'
        return render_template('index.html',post_success=post_success,message=message)
    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080))) #for running in cloud9
    # app.run(debug=True, port=5000)  