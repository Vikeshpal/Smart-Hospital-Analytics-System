# prediction.py
# Standalone script to test the trained ML model from the command line.
import joblib
import pandas as pd

# Load Saved Model
model = joblib.load("models/disease_prediction_model.pkl")

print("Model Loaded Successfully ✅")

age = int(input("Enter Age: "))
gender = int(input("Enter Gender (Male=1, Female=0): "))
bp = int(input("Enter Blood Pressure: "))
sugar = int(input("Enter Sugar Level: "))
bmi = float(input("Enter BMI: "))
heart_rate = int(input("Enter Heart Rate: "))
smoking = int(input("Smoking? (Yes=1, No=0): "))
alcohol = int(input("Alcohol? (Yes=1, No=0): "))
exercise = int(input("Exercise (High=0, Low=1, Medium=2): "))
age_group = int(input("Age Group (Young Adult=2, Adult=0, Senior=1): "))
bmi_category = int(input("BMI Category (Normal=0, Obese=1, Overweight=2): "))

new_patient = pd.DataFrame({

    "Age":[age],
    "Gender":[gender],
    "Blood_Pressure":[bp],
    "Sugar_Level":[sugar],
    "BMI":[bmi],
    "Heart_Rate":[heart_rate],
    "Smoking":[smoking],
    "Alcohol":[alcohol],
    "Exercise":[exercise],
    "Age_Group":[age_group],
    "BMI_Category":[bmi_category]

})


prediction = model.predict(new_patient)

print(prediction)

disease_map = {
    0: "Diabetes",
    1: "Healthy",
    2: "Heart Disease"
}

print("\nPredicted Disease:", disease_map[prediction[0]])