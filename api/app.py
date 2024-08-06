from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np  # Ensure NumPy is imported
import os

app = FastAPI()
current_dir = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

# Load the model using joblib with error handling
try:
    model_path = os.path.join(os.path.dirname(__file__), "models", "titanic_model.pkl")
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {model_path}")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Define Pydantic BaseModel for input validation
class InputData(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

# Homepage route to render the form
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Prediction endpoint
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pclass: int = Form(...),
    Sex: str = Form(...),
    Age: float = Form(...),
    SibSp: int = Form(...),
    Parch: int = Form(...),
    Fare: float = Form(...),
    Embarked: str = Form(...)
):
    try:
        # Validate input using Pydantic model
        input_data = InputData(
            Pclass=Pclass,
            Sex=Sex,
            Age=Age,
            SibSp=SibSp,
            Parch=Parch,
            Fare=Fare,
            Embarked=Embarked
        )

        # Convert validated input to a DataFrame for prediction
        input_df = pd.DataFrame([input_data.dict()])

        # Make prediction using the loaded model
        prediction = model.predict(input_df)

        # Assuming prediction is a single value, convert it to Python native type
        prediction_value = prediction.item()  # Convert numpy.int64 to int

        # Return prediction as part of the response rendered by the template
        return templates.TemplateResponse(
            "form.html", 
            {"request": request, "prediction": prediction_value}
        )

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"ValueError: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
