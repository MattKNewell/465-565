
## The image guessing game.
---
**Description**
Display an arbitrary number of images generated from Lorem Picsum.
Pick a single random image to be the correct answer.
Use Google Vision Api Label Detection to display descriptions
of the images and allow the user to try their hand at matching the
description to the image.

---
This app is hosted by Google Cloud Platform using App Engine at
this url.  <https://ivory-antler-233122.appspot.com/>

Create your own api key:
#### create a service account
<https://console.cloud.google.com/apis/credentials> 
#### Create a service account Key
Click Create Credentials then Service Key Account
This should start downloading a json file which is your service key account.

To run this locally:
#### Let google know where you key is held.
1. `export GOOGLE_APPLICATION_CREDENTIALS=key.json`
#### Set up your loval environment
2. `virtualenv env; source env/bin/activate; pip install -r requirements.txt`
Run the app!
3. `python main.py`
