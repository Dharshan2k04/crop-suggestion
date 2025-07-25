import numpy as np
from keras.models import load_model
import pandas as pd

# Load the LSTM model
model = load_model("lstm_model/crop_lstm_model.h5")

# Load and sort crop labels (assumes LabelEncoder-style alphabetical order)
df = pd.read_csv("data/Crop_recommendation.csv")
crop_labels = sorted(df["label"].unique())

def predict_crop(n, p, k, temperature, humidity, rainfall, ph):
    # Create input array
    input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

    # Reshape to match LSTM input format (samples, timesteps, features)
    input_reshaped = input_data.reshape(1, 1, 7)

    # Predict and get crop name
    prediction = model.predict(input_reshaped)
    predicted_index = np.argmax(prediction)
    return crop_labels[predicted_index]
