nclude the Dropbox SDK libraries
from dropbox import client, rest, session
import webbrowser

# Get your app key and secret from the Dropbox developer website
APP_KEY = 'f0y4cq0z9zdfved'
APP_SECRET = '940q0pg1uhh9x4w'

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()

url = sess.build_authorize_url(request_token, 'http://www.contrib.andrew.cmu.edu/~pwei/TartanHacks/')

# Make the user sign in and authorize this token

webbrowser.open_new(url)

raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'

access_token = sess.obtain_access_token(request_token)

client = client.DropboxClient(sess)
print "linked account:", client.account_info()



