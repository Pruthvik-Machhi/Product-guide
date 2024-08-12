import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

# Load the saved model
with open('rdmodel2.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the saved scaler
with open('scalermn.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Title of the app
st.title("Mobile Phone Price Prediction")

# Input for 'brand'
brand = st.selectbox('Select Brand', ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi'])

# Input for 'color'
color = st.selectbox('Select Color', ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver'])

# Input for 'storage'
storage = st.selectbox('Select Storage (GB)', [128, 64, 256, 16, 32, 512])

# Input for 'system'
system = st.selectbox('Select Operating System', ['android', 'ios'])

# Input for 'processor_type'
processor_type = st.selectbox('Select Processor Type', ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung'])

# Input for 'resolution'
resolution = st.selectbox('Select Resolution', ['Full HD', '4K', 'HD', '2K'])

# Input for 'size'
size = st.selectbox('Select Screen Size (inches)', [6.7, 6.5, 6.4, 5.4, 5.5, 6.6, 5.0, 6.2, 6.8, 6.1, 6.0, 6.3, 4.7, 5.7, 5.8, 4.0, 5.2, 7.0, 7.6, 5.6, 5.9, 6.9, 1.8, 5.3])

# Min-Max Scaling for 'storage'
storage_scaled = scaler.transform(np.array([[0, storage, 0]]))[0][1]

# One-Hot Encoding for all categorical features
input_data = {}

# Encoding 'brand'
brands = ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi']
for b in brands:
    input_data[f'brand_{b}'] = 1 if brand == b else 0

# Encoding 'color'
colors = ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver']
for c in colors:
    input_data[f'color_{c}'] = 1 if color == c else 0

# Encoding 'storage'
input_data['storage'] = storage_scaled

# Encoding 'system'
systems = ['android', 'ios']
for sys in systems:
    input_data[f'system_{sys}'] = 1 if system == sys else 0

# Encoding 'processor_type'
processors = ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung']
for proc in processors:
    input_data[f'processor_type_{proc}'] = 1 if processor_type == proc else 0

# Encoding 'resolution'
resolutions = ['Full HD', '4K', 'HD', '2K']
for res in resolutions:
    input_data[f'resolution_{res}'] = 1 if resolution == res else 0

# Encoding 'size'
input_data['size'] = size

# Convert to numpy array and reshape for prediction
input_vector = np.array(list(input_data.values())).reshape(1, -1)

# Button for prediction
if st.button('Predict Price'):
    # Predict the price (scaled value)
    scaled_prediction = model.predict(input_vector)

    # Create a full array for inverse transformation
    full_array = np.array([[scaled_prediction[0], storage_scaled, size]])
    
    # Reverse Min-Max scaling for the predicted price
    predicted_price = scaler.inverse_transform(full_array)[0][0]

    # Display the predicted price
    st.write(f"Predicted Price: {predicted_price:,.2f}")

# Display selected inputs
st.write("Selected Brand:", brand)
st.write("Selected Color:", color)
st.write("Selected Storage (Scaled):", storage_scaled)
st.write("Selected Operating System:", system)
st.write("Selected Processor Type:", processor_type)
st.write("Selected Resolution:", resolution)
st.write("Selected Screen Size:", size)
