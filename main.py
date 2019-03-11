# [START app]
import logging
import random
# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


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

@app.route('/taggame')
def taggame():
    imageToTag = "https://picsum.photos/400/400?image=" + checkImage()
    promptData = detect_labels_uri(imageToTag)
    return render_template('tagGame.html', imageToTag=imageToTag, promptData=promptData)

@app.route('/tag-result', methods=['POST'])
def tagging():
    userInput = request.form['usertag']
    lastImage = request.form['correct']
    promptData = detect_labels_uri(lastImage)
    print(userInput + " " + lastImage)

    return render_template('tagResult.html', userInput=userInput, lastImage=lastImage, promptData=promptData)

@app.route('/game')
def game():

    selection1 = checkImage()
    selection2 = checkImage()
    selection3 = checkImage()
    selection4 = checkImage()
   # selection5 = checkImage()
   # selection6 = checkImage()
   # selection7 = checkImage()
   # selection8 = checkImage()
   # selection9 = checkImage()

    selectArray = ([selection1, selection2, selection3, selection4])# selection5, selection6,selection7, selection8, selection9])

    image1 = "https://picsum.photos/400/400?image=" + selection1
    image2 = "https://picsum.photos/400/400?image=" + selection2
    image3 = "https://picsum.photos/400/400?image=" + selection3
    image4 = "https://picsum.photos/400/400?image=" + selection4
    #image5 = "https://picsum.photos/400/400?image=" + selection5
    #image6 = "https://picsum.photos/400/400?image=" + selection6
    #image7 = "https://picsum.photos/400/400?image=" + selection7
    #image8 = "https://picsum.photos/400/400?image=" + selection8
    #image9 = "https://picsum.photos/400/400?image=" + selection9

    images = ([image1, image2, image3, image4])#, image5, image6,image7,image8,image9])
    randomIndex = random.randint(1,4)
    correctAnswer = selectArray[randomIndex-1]

    # this is the data we will prompt the user with so they can made an educated guess
    promptData = detect_labels_uri("https://picsum.photos/800/800?image=" + correctAnswer)

    return render_template('game.html', promptData=promptData, correctAnswer=correctAnswer, images=images)
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():

    userGuess = request.form['image_name']
    correctAnswer = "https://picsum.photos/400/400?image=" +  request.form['correctAnswer']
    imgObject = detect_labels_uri(userGuess)
    print("userGuess: " + userGuess)
    successOrFailure = "Wrong"
    print("CorrectAnswer: " + correctAnswer);
    if userGuess == correctAnswer:
        successOrFailure = "Correct"

    return render_template('submitted_form.html', imgObject=imgObject, userGuess=userGuess, successOrFailure=successOrFailure, correctAnswer=correctAnswer)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]


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

    image = vision.types.Image()
    image.source.image_uri = uri


    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

def getRandomNumber():
    randomNumber = random.randint(1,1084)
    return str(randomNumber)

def checkImage():
    rando1 = getRandomNumber()
    ranUrl = detect_labels_uri("https://picsum.photos/800/800?image=" + rando1)
    if not ranUrl:
      return checkImage()
    return str(rando1)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
