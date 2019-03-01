
##The image guessing game.
#####A small description
---
**Description**
Have an arbitrary number of images in resources folder.
 Use a random library to display 3 images to the user
 with top 3 descriptions and the user needs to guess
 which picture correlates with the descriptions.  

---

\fbox{Have an arbitrary number of images in resources folder.
 Use a random library to display 3 images to the user
 with top 3 descriptions and the user needs to guess
 which picture correlates with the descriptions.}


To run this locally:

#create a service account
`gcloud iam service-accounts create vision-quickstart --project pythonhotdawg`
#Create a service account Key
`gcloud iam service-accounts keys create key.json --iam-account vision-quickstart@pythonhotdawg.iam.gserviceaccount.com`

#Let google know where you key is held.
`export GOOGLE_APPLICATION_CREDENTIALS=key.json`

`virtualenv env; source env/bin/activate; pip install -r requirements.txt`
`python main.py`
