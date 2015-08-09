import requests
from flask import Flask, request, redirect

app = Flask(__name__)

GOOGLE_CLIENT_ID = '834450588178-tmqi729odq8h0vkbik3rk9rm4no4aqgp.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'epOQT9krb6yKrkj7tu74PBEy'


@app.route('/')
def index():

    # We are going to immediately redirect to Google. We could ask the user
    # to sign in by clicking a button, if this were a more interesting app.

    signin_url = 'https://accounts.google.com/o/oauth2/auth?'

    parameters = [
        'client_id={}'.format(GOOGLE_CLIENT_ID),
        'redirect_uri={}'.format('http://localhost:8080/oauth2callback'),
        'response_type=code',
        'scope=profile']

    signin_url += '&'.join(parameters)

    return redirect(signin_url)


@app.route('/oauth2callback')
def callback():
    code = request.args.get('code')
    error = request.args.get('error')
    if error:
        return("Error! {}".format(error))

    # Exchange the code for an access token

    token_url = 'https://accounts.google.com/o/oauth2/token'
    data = {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': 'http://localhost:8080/oauth2callback',
        'code': code,
        'grant_type': 'authorization_code'
    }

    r = requests.post(token_url, data=data)

    # In an ideal world we would store this token and use it to make all our
    # future API requests.
    token = r.json().get('access_token')

    # Now we're going to call a Google API, in this case the userinfo API

    r = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'.format(token))

    info = r.json()
    print info
    user_name = info.get('name')
    return "Thank you for signing in, {}".format(user_name)


if __name__ == "__main__":
    app.run(debug=True)