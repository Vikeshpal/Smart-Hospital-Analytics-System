import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def prepare_data(df):

    df = df.copy()

    label_columns = [
        "Gender",
        "Smoking",
        "Alcohol",
        "Exercise",
        "Age_Group",
        "BMI_Category",
        "Disease"
    ]

    encoders = {}

    for col in label_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df


def split_data(df):

    X = df.drop(["Patient_ID", "Disease"], axis=1)

    y = df["Disease"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def train_model(X_train, y_train):

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"\nModel Accuracy : {accuracy*100:.2f}%")

    return prediction


def save_model(model):

    joblib.dump(
        model,
        "models/disease_prediction_model.pkl"
    )

    print("\nModel Saved Successfully.")