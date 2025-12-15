from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load(r'C:\Users\areeb\Desktop\S5\ML\project\model.pkl')

@app.route("/")
def home():
    return "Medical Insurance Cost Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    x = np.array([[
        data["age"],
        data["bmi"],
        data["children"],
        data["sex"],
        data["smoker"],
        data["region"]
    ]])

    prediction = model.predict(x)[0]

    return jsonify({"predicted_cost": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
