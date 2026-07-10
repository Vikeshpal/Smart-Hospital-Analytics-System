import pandas as pd

from visualization import (
    age_distribution,
    disease_bar_chart,
    disease_pie_chart,
    bmi_box_plot
)

from data_cleaning import (
    check_missing_values,
    check_duplicate_values,
    dataset_information,
    statistical_summary
)

from feature_engineering import create_age_group,create_bmi_category

from model import prepare_data, split_data, train_model,evaluate_model,save_model

print("=" * 50)
print("SMART HOSPITAL ANALYTICS SYSTEM")
print("=" * 50)

# Load Dataset
df = pd.read_csv("dataset/hospital_data.csv")

df = create_age_group(df)

df = create_bmi_category(df)

encoded_df = prepare_data(df)

X_train, X_test, y_train, y_test = split_data(encoded_df)

model = train_model(X_train, y_train)

predictions = evaluate_model(model, X_test, y_test)

save_model(model)

print("\nModel Trained Successfully ✅")

print("\nTraining Data Shape:", X_train.shape)

print("Testing Data Shape:", X_test.shape)

print("\nAge")
print(df[["Age","Age_Group"]])

print("\nBMI Category:")
print(df[["BMI", "BMI_Category"]])

print("\nDataset Loaded Successfully ✅")

# First 5 Records
print("\nFirst 5 Records:")
print(df.head())

print("\nEncoded Dataset:")
print(encoded_df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

dataset_information(df)

statistical_summary(df)

check_missing_values(df)

check_duplicate_values(df)

# print("\nBMI Category:")
# print(df[["BMI", "BMI_Category"]])

# Dataset Information
# print("\nData Information:")
# df.info()

# # Statistical Summary
# print("\nStatistical Summary:")
# print(df.describe())

# # Missing Values
# print("\nMissing Values:")
# print(df.isnull().sum())

# # Duplicate Rows
# print("\nDuplicate Rows:")
# print(df.duplicated().sum())

# Disease Count
print("\nDisease Count:")
print(df["Disease"].value_counts())

# ----------------------------
# Visualization Functions
# ----------------------------

age_distribution(df)

disease_bar_chart(df)

disease_pie_chart(df)

bmi_box_plot(df)

print("\nAge Group:")
print(df[["Age", "Age_Group"]])