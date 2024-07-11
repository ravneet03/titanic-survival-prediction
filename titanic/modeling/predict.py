import mlflow.sklearn
import pandas as pd

model = mlflow.sklearn.load_model("models/model")

def predict(input_data):
    df = pd.DataFrame(input_data)
    predictions = model.predict(df)
    return predictions
