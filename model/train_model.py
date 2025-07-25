import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data/Crop_recommendation.csv")

# Feature and label split
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].values
y = df['label'].values

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Reshape for LSTM
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

# Build model
model = Sequential([
    LSTM(64, input_shape=(X.shape[1], X.shape[2])),
    Dense(64, activation='relu'),
    Dense(len(np.unique(y_encoded)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=25, batch_size=32, validation_data=(X_test, y_test))

# Save
model.save("lstm_model/crop_lstm_model.h5")
