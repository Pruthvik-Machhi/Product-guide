import pandas as pd
import pickle

def load_model_and_scaler():
    """
    Load the model and scaler from disk.
    """
    with open(r'D:\GthubFiles\Product-guide\models\rdmodel2.pkl', 'rb') as file:
        model = pickle.load(file)
    with open(r'D:\GthubFiles\Product-guide\models\scalermn.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return model, scaler

def load_data():
    """
    Load the dataset from disk.
    """
    return pd.read_csv(r'D:\GthubFiles\Product-guide\data\data.csv')
