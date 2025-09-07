from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.utils.common import decodeImage
from src.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


# ======================== ROUTES ========================

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    # OLD: return render_template('index.html')
    # NEW: Serve home.html as landing page
    return render_template('home.html')


@app.route("/form", methods=['GET'])
@cross_origin()
def form():
    # NEW: Upload + Predict form page
    return render_template('form.html')


@app.route("/result", methods=['GET'])
@cross_origin()
def resultPage():
    # NEW: Just serves result page template (JS will insert result dynamically)
    return render_template('result.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # os.system("python main.py")   # OLD training command
    os.system("dvc repro")          # NEW: Use DVC repro instead of python main.py
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    # decode incoming base64 image
    image = request.json['image']
    decodeImage(image, clApp.filename)

    # run prediction
    result = clApp.classifier.predict()

    # return result (used by JS in form.html)
    return jsonify(result)


# ======================== MAIN ========================

if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080, debug=True) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80) #for AZURE
