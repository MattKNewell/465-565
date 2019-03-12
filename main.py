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
    # print(promptData)
    YesOrNo = "Nope"
    for Label in promptData:
        if("dog" in Label.description):
            YesOrNo = "YES"
    return render_template('hotdog.html', YesOrNo=YesOrNo, promptData=promptData, hotdogurl=hotdogurl)

@app.route('/taggame')
def taggame():
    imageToTag = "static/images/" +  getRandomNumber() + ".jpg"
    promptData = run_quickstart(imageToTag)
    return render_template('tagGame.html', imageToTag=imageToTag, promptData=promptData)

@app.route('/tag-result', methods=['POST'])
def tagging():
    userInput = request.form['usertag']
    lastImage = request.form['correct']
    promptData = run_quickstart(lastImage)
    # print(userInput + " " + lastImage)

    return render_template('tagResult.html', userInput=userInput, lastImage=lastImage, promptData=promptData)

@app.route('/')
def game():

    selection1 = getRandomNumber()
    selection2 = getRandomNumber()
    selection3 = getRandomNumber()
    selection4 = getRandomNumber()
    selection5 = getRandomNumber()
    selection6 = getRandomNumber()
    selection7 = getRandomNumber()
    selection8 = getRandomNumber()
    selection9 = getRandomNumber()
    selection10 = getRandomNumber()
    selection11 = getRandomNumber()
    selection12 = getRandomNumber()

    #TODO Make selections unqiue

    selectArray = ([selection1, selection2, selection3, selection4, selection5, selection6,selection7, selection8, selection9,selection10,selection11,selection12])

    image1 = "static/images/" + selection1 + ".jpg"
    image2 = "static/images/" + selection2 + ".jpg"
    image3 = "static/images/" + selection3 + ".jpg"
    image4 = "static/images/" + selection4 + ".jpg"
    image5 = "static/images/" + selection5 + ".jpg"
    image6 = "static/images/" + selection6 + ".jpg"
    image7 = "static/images/" + selection7 + ".jpg"
    image8 = "static/images/" + selection8 + ".jpg"
    image9 = "static/images/" + selection9 + ".jpg"
    image10 = "static/images/" + selection10 + ".jpg"
    image11= "static/images/" + selection11 + ".jpg"
    image12 = "static/images/" + selection12 + ".jpg"

    # checkimage(image1)
    # checkimage(image2)
    # checkimage(image3)
    # checkimage(image4)
    # checkimage(image5)
    # checkimage(image6)
    # checkimage(image7)
    # checkimage(image8)
    # checkimage(image9)

    images = ([image1, image2, image3, image4, image5, image6,image7,image8,image9,image10,image11,image12])
    randomIndex = random.randint(1,12)
    correctAnswer = selectArray[randomIndex-1]

    # this is the data we will prompt the user with so they can made an educated guess
    promptData = run_quickstart("static/images/" + correctAnswer + ".jpg")
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
        image_name)

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

    image = vision.types.Image()
    image.source.image_uri = uri


    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

def getRandomNumber():
    randomNumber = random.randint(1,906)
    return str(randomNumber)

# by using the api function call we create more api calls than needed
def checkImage():
    rando1 = getRandomNumber()
    ranUrl = detect_labels_uri("https://picsum.photos/800/800?image=" + str(rando1) )
    if not ranUrl:
      return checkImage()
    return str(rando1)

def checkimage(image):
    rando1 = getRandomNumber()
    ranUrl = "static/images/" + getRandomNumber() + ".jpg"
    if not ranUrl:
      return checkimage()
    return str(rando1)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
