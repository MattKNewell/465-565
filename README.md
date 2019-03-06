
## The image guessing game.
---
**Description**
Display three images generated from Lorem Picsum.
Pick an arbitrary single image to be the correct answer.
Use Google Vision Api Label Detection to display descriptions
of the images and allow the user to try their hand at matching the
description to the image.

---
This app is hosted by Google Cloud Platform using App Engine at
this url.  <https://ivory-antler-233122.appspot.com/>

Create your own api key:
#### create a service account
1. `gcloud iam service-accounts create vision-quickstart --project pythonhotdawg`
#### Create a service account Key
2. `gcloud iam service-accounts keys create key.json --iam-account vision-quickstart@pythonhotdawg.iam.gserviceaccount.com`

To run this locally:
#### Let google know where you key is held.
3. `export GOOGLE_APPLICATION_CREDENTIALS=key.json`

4. `virtualenv env; source env/bin/activate; pip install -r requirements.txt`
Run the app!
5. `python main.py`
