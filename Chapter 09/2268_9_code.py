import json
import numpy as np
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from sklearn.linear_model import LinearRegression
from PIL import Image
import torch
from torchvision import models, transforms

# Initialize LangChain AI Model
chat_model = ChatOpenAI()

def query_ai(question):
    response = chat_model([HumanMessage(content=question)])
    return response.content

def collect_data():
    data = {
        "temperature": np.random.uniform(15, 35),
        "humidity": np.random.uniform(20, 90),
        "soil_moisture": np.random.uniform(10, 60),
        "rainfall": np.random.uniform(0, 200),
        "historical_yield": np.random.uniform(1, 5),
    }
    return data

def predict_yield(data):
    model = LinearRegression()
    X_train = np.array([[15, 20, 10, 50], [30, 80, 50, 100], [25, 60, 40, 75]])
    y_train = np.array([1.5, 4.0, 3.2])
    model.fit(X_train, y_train)
    X_test = np.array([[data['temperature'], data['humidity'], data['soil_moisture'], data['rainfall']]])
    return model.predict(X_test)[0]

def generate_recommendations(data):
    if data['soil_moisture'] < 20:
        return "Increase irrigation to prevent drought stress."
    elif data['temperature'] > 30:
        return "Consider heat-resistant crop varieties."
    else:
        return "Conditions are optimal for crop growth."

sensor_data = collect_data()
yield_prediction = predict_yield(sensor_data)
decision_recommendation = generate_recommendations(sensor_data)

print("Sensor Data:", json.dumps(sensor_data, indent=2))
print("Predicted Yield:", yield_prediction, "tons per hectare")
print("Farming Recommendation:", decision_recommendation)
