import streamlit as st
from product_guide.data_converter import scale_storage, encode_features
from product_guide.retrieval_generation import find_top_matching, get_recommendations
from product_guide.data_ingestion import load_model_and_scaler, load_data
from chatbot.chatbotui import chatbot_interface

st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .main-container {
        display: flex;
        flex-direction: row;
        gap: 2rem;
    }
    .navigation-container {
        min-width: 200px;
        padding: 1rem;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .content-container {
        flex-grow: 1;
    }
    .block-container {
        padding: 1rem;
    }
    button.css-1q8dd3e {
        margin-top: 1rem;
        background-color: #007BFF !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

model, scaler = load_model_and_scaler()

st.title("Smart Mobile Guide")
selected_page = st.radio(
    "Navigation",
    ["Smart Mobile Prediction", "Chatbot"],
    key="navigation",
    horizontal=True, 
)

def prediction_interface():
    st.header("Device Recommendation")
    col1, col2, col3 = st.columns(3)

    with col1:
        brand = st.selectbox('Select Brand', ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi'])
        color = st.selectbox('Select Color', ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver'])
        storage = st.selectbox('Select Storage (GB)', [128, 64, 256, 16, 32, 512])

    with col2:
        system = st.selectbox('Select Operating System', ['android', 'other'])
        processor_type = st.selectbox('Select Processor Type', ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung'])

    with col3:
        resolution = st.selectbox('Select Resolution', ['Full HD', '4K', 'HD', '2K'])
        size = st.selectbox('Select Screen Size (inches)', [6.7, 6.5, 6.4, 5.4, 5.5, 6.6, 5.0, 6.2, 6.8, 6.1, 6.0, 6.3, 4.7, 5.7, 5.8, 4.0, 5.2, 7.0, 7.6, 5.6, 5.9, 6.9, 1.8, 5.3])

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
        input_features = encode_features(brand, color, storage, system, processor_type, resolution, size, scaler)
        predicted_price = get_recommendations(model, scaler, input_features, storage, size)
        st.write(f"Predicted Price: {predicted_price:,.2f}")

        rdf = load_data()
        st.write("Recommended devices Based on Predicted Price:")
        recommended_device = find_top_matching(rdf[rdf['price'] <= predicted_price], selected_values, top_n=5)
        st.table(recommended_device)

    budget1 = st.number_input("Enter your budget (in the same currency as predicted price):")
    if st.button('Predict Devices for Budget'):
        rdf = load_data()
        filtered_laptops = rdf[rdf['price'] <= budget1]
        if filtered_laptops.empty:
            st.write(f"No devices are available below the price of {budget1}.")
        else:
            st.write("Recommended devices Based on Budget:")
            recommended_device = find_top_matching(filtered_laptops, selected_values, top_n=5)
            st.table(recommended_device)

if selected_page == "Smart Mobile Prediction":
    prediction_interface()
elif selected_page == "Chatbot":
    chatbot_interface()
