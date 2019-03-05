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

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START form]
@app.route('/')
def form():

    return render_template('index.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    
    image_name =request.form['image_name']
    imgObject = run_quickstart(image_name)
    image_name = "https://storage.googleapis.com/image_guess_game/" + image_name
    print(image_name)

    # [END submitted]
    # [START render_template]
    return render_template('submitted_form.html', imgObject=imgObject, image_name=image_name)
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

    print('Labels:')
    for label in labels:
        print(label.description)
     #[END vision_quickstart]
    return labels


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
