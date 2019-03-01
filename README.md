
## The image guessing game.
---
**Description**
Have an arbitrary number of images in resources folder.
 Use a random library to display 3 images to the user
 with top 3 descriptions and the user needs to guess
 which picture correlates with the descriptions.  

---


To run this locally:

#### create a service account
1. `gcloud iam service-accounts create vision-quickstart --project pythonhotdawg`
#### Create a service account Key
2. `gcloud iam service-accounts keys create key.json --iam-account vision-quickstart@pythonhotdawg.iam.gserviceaccount.com`

#### Let google know where you key is held.
3. `export GOOGLE_APPLICATION_CREDENTIALS=key.json`

4. `virtualenv env; source env/bin/activate; pip install -r requirements.txt`
5. `python main.py`
