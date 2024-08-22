import streamlit as st
import numpy as np
import pandas as pd
import pickle
from pyprik import find_top_matching
with open('rdmodel2.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scalermn.pkl', 'rb') as file:
    scaler = pickle.load(file)
st.title("Mobile Phone Price Prediction")

def get_input_features():
    brand = st.selectbox('Select Brand', ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi'])
    color = st.selectbox('Select Color', ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver'])
    storage = st.selectbox('Select Storage (GB)', [128, 64, 256, 16, 32, 512])
    system = st.selectbox('Select Operating System', ['android', 'ios'])
    processor_type = st.selectbox('Select Processor Type', ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung'])
    resolution = st.selectbox('Select Resolution', ['Full HD', '4K', 'HD', '2K'])
    size = st.selectbox('Select Screen Size (inches)', [6.7, 6.5, 6.4, 5.4, 5.5, 6.6, 5.0, 6.2, 6.8, 6.1, 6.0, 6.3, 4.7, 5.7, 5.8, 4.0, 5.2, 7.0, 7.6, 5.6, 5.9, 6.9, 1.8, 5.3])
    return brand, color, storage, system, processor_type, resolution, size

def scale_storage(storage):
    return scaler.transform(np.array([[0, storage, 0]]))[0][1]

def encode_features(brand, color, storage, system, processor_type, resolution, size):
    input_data = {}
    brands = ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi']
    colors = ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver']
    systems = ['android', 'ios']
    processors = ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung']
    resolutions = ['Full HD', '4K', 'HD', '2K']
    
    for b in brands:
        input_data[f'brand_{b}'] = 1 if brand == b else 0
    for c in colors:
        input_data[f'color_{c}'] = 1 if color == c else 0
    input_data['storage'] = scale_storage(storage)
    for sys in systems:
        input_data[f'system_{sys}'] = 1 if system == sys else 0
    for proc in processors:
        input_data[f'processor_type_{proc}'] = 1 if processor_type == proc else 0
    for res in resolutions:
        input_data[f'resolution_{res}'] = 1 if resolution == res else 0
    input_data['size'] = size
    return input_data

def main():
    brand, color, storage, system, processor_type, resolution, size = get_input_features()

    input_data = encode_features(brand, color, storage, system, processor_type, resolution, size)
    input_vector = np.array(list(input_data.values())).reshape(1, -1)
    selected_values = {
    'brand': brand,
    'color': color,
    'storage': storage,
    'system': system,
    'processor_type': processor_type,
    'resolution': resolution,
    'size': size
}
    if st.button('Predict Price'):
        scaled_prediction = model.predict(input_vector)
        full_array = np.array([[scaled_prediction[0], scale_storage(storage), size]])
        predicted_price = scaler.inverse_transform(full_array)[0][0]
        st.write(f"Predicted Price: {predicted_price:,.2f}")

        rdf = pd.read_csv('rdf1.csv')  


        st.write("Recommended Laptops Based on Predicted Price:")
        recommended_laptops = find_top_matching(rdf[rdf['price'] <= predicted_price], selected_values, top_n=5)
        st.table(recommended_laptops)

    # Budget input for additional recommendations
    budget1 = st.number_input("Enter your budget (in the same currency as predicted price):")
    if st.button('Predict Price for budget'):
        rdf = pd.read_csv('rdf1.csv') 

        st.write("Recommended Laptops Based on Budget:")
        recommended_laptops = find_top_matching(rdf[rdf['price'] <= budget1], selected_values, top_n=5)
        st.table(recommended_laptops)

if __name__ == "__main__":
    main()
