from flask import Flask, jsonify, request
from prediction import get_prediction

app =Flask(__name__)

@app.route("/predict_digit", methods =["POST"])
def prediction():
    image = request.files.get("digit")
    predict = get_prediction(image)

    return jsonify({"predict":predict})

if __name__ =="__main__":
    app.run(debug = True)

