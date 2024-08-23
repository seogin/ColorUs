from os import walk
from detect_face import DetectFace
from color_extract import DominantColors
from color_converter import rgb2lab
from colorsys import rgb_to_hsv
import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Reusable function to process images
def process_image(file_path):
    face = DetectFace(file_path).get_face()
    
    if len(face) > 0:
        colors, _ = DominantColors(face).getHistogram()
        data = []
        for color in colors:
            lab = rgb2lab(color)
            hsv = rgb_to_hsv(*color)

            data.append(lab[2] / 128)
            data.append(((hsv[1] * 255) - 128) / 255)
            data.append((hsv[2] - 128) / 255)

        if len(data) == 3:
            pickle_path = os.path.join(os.path.dirname(__file__), "../personalColor.pickle")
            with open(pickle_path, "rb") as pickle_in:
                model = pickle.load(pickle_in)
            predict = model.predict([data])
            return predict[0]
        else:
            return "Not enough data"
    else:
        return "No face detected"

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"result": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"result": "No selected file"}), 400
    
    # Save the uploaded file to a temporary location
    file_path = os.path.join("/tmp", file.filename)
    file.save(file_path)
    
    result = process_image(file_path)
    
    if result == "No face detected" or result == "Not enough data":
        return jsonify({"result": result}), 400
    
    return jsonify({"result": result}), 200

def main():
    path = "../test"

    directories = next(walk(path))[1]

    for directory in directories:
        images = next(walk(f"{path}/{directory}"))[2]
        for image in images:
            if image == ".DS_Store":
                continue
            file_path = f"{path}/{directory}/{image}"
            result = process_image(file_path)
            print(f"Actual: {directory}      Prediction: {result}")

if __name__ == "__main__":
    main()  # Run the main function for batch processing
    # app.run(debug=True, port=5000)  # Uncomment to run the Flask server
