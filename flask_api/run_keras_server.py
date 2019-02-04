"""@desc 
		Flask server for keras model serving

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2018-12-31 03:31:43
 		@modify date 2018-12-31 03:31:43

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """


import io
import logging
import os
import threading

import flask
import numpy as np
from flask import render_template
import tensorflow as tf
from celery import Celery
from consts import *
# import the necessary packages
from keras.applications import ResNet50, imagenet_utils
from keras.applications.resnet50 import ResNet50
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
from utils import prepare_image

# from google.appengine.ext import vendor
# vendor.add(LIB_DIR)




model = None
graph = None
# initialize our Flask application and the Keras model
app = flask.Flask(__name__, template_folder=TEMPLATE_DIR)
#get redis connection from env var , else use default
app.config['CELERY_BROKER_URL'] = os.environ.get('REDIS_URL', CELERY.BROKER_URL)
app.config['CELERY_RESULT_BACKEND'] = os.environ.get('REDIS_URL', CELERY.RESULT_BACKEND)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
print(os.environ.get("PORT", "Port does not exist"))


@app.before_first_request
def app_load_model():
    """load the model in a non blocking thread
    """
    def non_blocking_load():
        """Loads the model from keras
        """
        global model, graph
        print(LOADING_MESSAGE)
        # model = load_model(MODEL_LOCATION)
        model = ResNet50(weights="imagenet")
        print("Completed loading model... waiting for requests")
        graph = tf.get_default_graph()
    thread = threading.Thread(target=non_blocking_load)
    thread.start()

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route("/")
def home():
    """index page for the predict api"""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """initialize the data dictionary that will be returned from the
        view
    
    :rtype: `flask.json`
    """
    global model, graph
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image=image, target_size=TARGET_SIZE)

            # classify the input image and then initialize the list
            # of predictions to return to the client
            #run predictions asynchronously and get output with collect()
            with graph.as_default():
                preds = model.predict(image)
            print(flask.request.args)
            if flask.request.args.get("top"):
                top = flask.request.args.get("top")
                results = imagenet_utils.decode_predictions(preds, top=top)
            else:
                results = imagenet_utils.decode_predictions(preds, top=DEFAULT_PREDICTION_NUMBER)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    #locally run debug
    app.run(debug=True, port='8008')
