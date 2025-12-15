from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load(r"C:\Users\areeb\Desktop\S5\ML\project\model.pkl")

@app.post("/predict")
def predict(age:int, bmi:float, children:int, sex:int, smoker:int, region:int):

    x = np.array([[age, bmi, children, sex, smoker, region]])
    prediction = model.predict(x)[0]

    return {
        "predicted_insurance_cost": float(prediction)
    }
