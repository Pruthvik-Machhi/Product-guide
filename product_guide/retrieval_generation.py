import numpy as np

def find_top_matching(data, selected_values, top_n=5):
    """
    Find the top matching items based on the selected values.
    """
    return data.head(top_n)

def get_recommendations(model, scaler, input_vector, storage, size):
    """
    Predict price and return the unscaled prediction.
    """
    scaled_prediction = model.predict(input_vector)
    full_array = np.array([[scaled_prediction[0], scaler.transform([[0, storage, 0]])[0][1], size]])
    predicted_price = scaler.inverse_transform(full_array)[0][0]
    return predicted_price
