# [START app]
import logging
import random
# [START imports]
from flask import Flask, render_template, request, session
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START Routes ]
@app.route('/info')
def home():
    return render_template('index.html')

@app.route('/links')
def hotdogForm():
    return render_template('hotdogForm.html')

@app.route('/hotdog', methods=['POST'])
def hotdog():
    hotdogurl = request.form['hotdog']
    promptData = detect_labels_uri(hotdogurl)
    YesOrNo = "Nope"
    for Label in promptData:
        if("dog" in Label.description):
            YesOrNo = "YES"
    return render_template('hotdog.html', YesOrNo=YesOrNo, promptData=promptData, hotdogurl=hotdogurl)

@app.route('/taggame')
def taggame():
    imageToTag = str(get1RandomNumber() )
    promptData = run_quickstart(imageToTag)
    return render_template('tagGame.html', imageToTag=imageToTag, promptData=promptData)

@app.route('/tag-result', methods=['POST'])
def tagging():
    userInput = request.form['usertag']
    lastImage = request.form['correct']
    promptData = run_quickstart(lastImage)
    return render_template('tagResult.html', userInput=userInput, lastImage=lastImage, promptData=promptData)

@app.route('/')
def game():


    selectArray = getRandomNumber()

    image1 = "static/images/" + str(selectArray[0]) + ".jpg"
    image2 = "static/images/" + str(selectArray[1]) + ".jpg"
    image3 = "static/images/" + str(selectArray[2]) + ".jpg"
    image4 = "static/images/" + str(selectArray[3]) + ".jpg"
    image5 = "static/images/" + str(selectArray[4]) + ".jpg"
    image6 = "static/images/" + str(selectArray[5]) + ".jpg"
    image7 = "static/images/" + str(selectArray[6]) + ".jpg"
    image8 = "static/images/" + str(selectArray[7]) + ".jpg"
    image9 = "static/images/" + str(selectArray[8]) + ".jpg"
    image10 = "static/images/" + str(selectArray[9]) + ".jpg"
    image11= "static/images/" + str(selectArray[10]) + ".jpg"
    image12 = "static/images/" + str(selectArray[11]) + ".jpg"

    images = ([image1, image2, image3, image4, image5, image6,image7,image8,image9,image10,image11,image12])
    randomIndex = random.randint(1,12)
    correctAnswer = selectArray[randomIndex-1]

    # this is the data we will prompt the user with so they can made an educated guess
    promptData = run_quickstart("static/images/" + str(correctAnswer) + ".jpg")
    #I should try to gert a secret working in order to make one less api call
    # session['my_var'] = promptData
    return render_template('game.html', promptData=promptData, correctAnswer=correctAnswer, images=images)
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    # imgObject = session.get('my_var', None)
    userGuess = request.form['image_name']
    imgObject = run_quickstart(userGuess)
    correctAnswer = "static/images/" + request.form['correctAnswer']+ ".jpg"
    successOrFailure = "Wrong"
    if userGuess == correctAnswer:
        successOrFailure = "Correct"

    return render_template('submitted_form.html', imgObject=imgObject, userGuess=userGuess, successOrFailure=successOrFailure, correctAnswer=correctAnswer)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

def run_quickstart(image_name):
    import io
    import os

    from google.cloud import vision
    from google.cloud.vision import types

    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        image_name)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def detect_labels_uri(uri):
    import io
    import os
    from google.cloud import vision
    from google.cloud.vision import types

    client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

def getRandomNumber():
   return random.sample(range(1, 907), 12)


def checkImage():
    rando1 = getRandomNumber()
    ranUrl = detect_labels_uri("https://picsum.photos/800/800?image=" + str(rando1) )
    if not ranUrl:
      return checkImage()
    return str(rando1)

def get1RandomNumber():
    return "static/images/" + str( random.randint(1,906) )+ ".jpg"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
