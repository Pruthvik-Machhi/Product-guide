import numpy as np
import pandas as pd


def scale_storage(storage, scaler):
    """
    Scale storage using the scaler.
    """
    return scaler.transform(np.array([[0, storage, 0]]))[0][1]

def encode_features(brand, color, storage, system, processor_type, resolution, size, scaler):
    """
    Encode the input features for prediction.
    """
    input_data = {}
    brands = ['redmi', 'oppo', 'oneplus', 'other', 'infinix', 'samsung', 'vivo', 'motorola', 'realme', 'mi', 'tecno', 'xiaomi']
    colors = ['black', 'green', 'white', 'blue', 'gold', 'purple', 'red', 'grey', 'silver']
    systems = ['android', 'other']
    processors = ['mediatek', 'unknown', 'qualcomm', 'other', 'unisoc', 'samsung']
    resolutions = ['Full HD', '4K', 'HD', '2K']

    for b in brands:
        input_data[f'brand_{b}'] = 1 if brand == b else 0
    for c in colors:
        input_data[f'color_{c}'] = 1 if color == c else 0
    input_data['storage'] = scale_storage(storage, scaler)
    for sys in systems:
        input_data[f'system_{sys}'] = 1 if system == sys else 0
    for proc in processors:
        input_data[f'processor_type_{proc}'] = 1 if processor_type == proc else 0
    for res in resolutions:
        input_data[f'resolution_{res}'] = 1 if resolution == res else 0
    input_data['size'] = size
    return np.array(list(input_data.values())).reshape(1, -1)

def dataconverter():
    from langchain.schema import Document
    product_data = pd.read_csv(r"D:\pg\Product-guide\data\data.csv")

    data = product_data[["price", "brand", "color", "storage", "system", "processor_type", "resolution", "size", "Model_name"]]

    product_list = []

    for index, row in data.iterrows():
        product = {
            "price": row["price"],
            "brand": row["brand"],
            "color": row["color"],
            "storage": row["storage"],
            "system": row["system"],
            "processor_type": row["processor_type"],
            "resolution": row["resolution"],
            "size": row["size"],
            "model_name": row["Model_name"]
        }

        product_list.append(product)

    docs = []
    for entry in product_list:
        metadata = {
            "price": entry["price"],
            "brand": entry["brand"],
            "color": entry["color"],
            "storage": entry["storage"],
            "system": entry["system"],
            "processor_type": entry["processor_type"],
            "resolution": entry["resolution"],
            "size": entry["size"],
            "model_name": entry["model_name"]
        }
        doc = Document(page_content=str(metadata), metadata=metadata)
        docs.append(doc)

    return docs
