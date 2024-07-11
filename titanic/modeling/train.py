import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Define data paths
PROCESSED_DATA_PATH = '/home/ravneet-singh/machine-learning/titanic-survival-prediction/data/processed/titanic_processed.csv'
MODEL_PATH = '/home/ravneet-singh/machine-learning/titanic-survival-prediction/models/titanic_model.pkl'

def load_data():
    return pd.read_csv(PROCESSED_DATA_PATH)

def preprocess_data(df):
    y = df['Survived']
    X = df.drop('Survived', axis=1)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_pipeline():
    numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    categorical_features = ['Pclass', 'Sex', 'Embarked']
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier())])

    return pipeline

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
