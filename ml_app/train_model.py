# ml_app/train_model.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_and_save_model():
    # Load the Iris dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100)

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model to a file
    model_path = os.path.join(os.getcwd(), 'ml_app', 'iris_model.pkl')
    joblib.dump(model, model_path)

    print(f"Model trained and saved at {model_path}")

if __name__ == "__main__":
    train_and_save_model()
