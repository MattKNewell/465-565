# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import random
# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

def getRandomNumber():
    randomNumber = random.randint(1,1084)
    return str(randomNumber)

def checkImage():
    rando1 = getRandomNumber()
    ranUrl = detect_labels_uri("https://picsum.photos/800/800?image=" + rando1)
    if not ranUrl:
      return "0"
    return str(rando1)

# [START Routes ]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hotdog', methods=['POST'])
def hotdog():
    hotdogurl = request.form['hotdog']
    promptData = detect_labels_uri(hotdogurl)
    print(promptData)
    YesOrNo = "Nope"
    for Label in promptData:
        if("dog" in Label.description):
            print("YES")
            YesOrNo = "YES"
    return render_template('hotdog.html', YesOrNo=YesOrNo, promptData=promptData, hotdogurl=hotdogurl)

@app.route('/game')
def game():

    selection1 = checkImage()
    selection2 = checkImage()
    selection3 = checkImage()
    selection4 = checkImage()
    selection5 = checkImage()
    selection6 = checkImage()
    selection7 = checkImage()
    selection8 = checkImage()
    selection9 = checkImage()
    selection10 = checkImage()
    selection11 = checkImage()
    selection12 = checkImage()
    selection13 = checkImage()
    selection14 = checkImage()
    selection15 = checkImage()

    image1 = "https://picsum.photos/800/800?image=" + selection1
    image2 = "https://picsum.photos/800/800?image=" + selection2
    image3 = "https://picsum.photos/800/800?image=" + selection3
    image4 = "https://picsum.photos/800/800?image=" + selection4
    image5 = "https://picsum.photos/800/800?image=" + selection5
    image6 = "https://picsum.photos/800/800?image=" + selection6
    image7 = "https://picsum.photos/800/800?image=" + selection7
    image8 = "https://picsum.photos/800/800?image=" + selection8
    image9 = "https://picsum.photos/800/800?image=" + selection9
    image10 = "https://picsum.photos/800/800?image=" + selection10
    image11 = "https://picsum.photos/800/800?image=" + selection11
    image12 = "https://picsum.photos/800/800?image=" + selection12
    image13 = "https://picsum.photos/800/800?image=" + selection13
    image14 = "https://picsum.photos/800/800?image=" + selection14
    image15 = "https://picsum.photos/800/800?image=" + selection15

    images = ([image1, image2, image3, image4, image5, image6,image7,image8,image9,image10,image11,image12,image13,image14,image15])
    selectArray = ([selection1, selection2, selection3, selection4, selection5, selection6,selection7, selection8, selection9,selection10, selection11, selection12,selection13, selection14, selection15])
    randomIndex = random.randint(1,15)
    correctAnswer = selectArray[randomIndex-1]

    # this is the data we will prompt the user with so they can made an educated guess
    promptData = detect_labels_uri("https://picsum.photos/800/800?image=" + correctAnswer)
 
    return render_template('game.html', promptData=promptData, correctAnswer=correctAnswer, images=images)
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():

    userGuess = request.form['image_name']
    correctAnswer = "https://picsum.photos/800/800?image=" +  request.form['correctAnswer']
    imgObject = detect_labels_uri(userGuess)
    print("userGuess: " + userGuess)
    successOrFailure = "Wrong"
    print("CorrectAnswer: " + correctAnswer);
    if userGuess == correctAnswer:
        successOrFailure = "Correct"

    #userGuess = "https://storage.googleapis.com/image_guess_game/" + userGuess
    # [END submitted]
    # [START render_template]
    return render_template('submitted_form.html', imgObject=imgObject, userGuess=userGuess, successOrFailure=successOrFailure, correctAnswer=correctAnswer)
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]


def run_quickstart(image_name):
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        "resources/" + image_name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #print('Labels:')
    #for label in labels:
        #print(label.description)
     #[END vision_quickstart]
    return labels



def detect_labels_uri(uri):
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    #file_name = os.path.join(
        #os.path.dirname(__file__),
        #"resources/" + image_name)
    image = vision.types.Image()
    image.source.image_uri = uri
    # Loads the image into memory
    #with io.open(file_name, 'rb') as image_file:
        #content = image_file.read()

    #image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #print('Labels:')
    #for label in labels:
        #print(label.description)
     #[END vision_quickstart]
    return labels


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
