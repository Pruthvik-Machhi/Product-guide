# Smart Mobile Guide

This project is designed to predict the price of devices based on user-specified features and recommend devices that match the desired features within a given budget. It leverages a custom Python package, published on PyPI, for seamless data preprocessing, analysis, and recommendations.

---
## **Video Demo**: [YouTube Video](https://www.youtube.com/watch?v=cBVQuHSqev4)  

<p align="center">
  <img src="Research/Screenshot 2024-12-01 144139.png" alt="Screenshot 1" width="45%">
  <img src="Research/Screenshot 2024-12-01 144216.png" alt="Screenshot 2" width="45%">
</p>

## Features

- **Price Prediction**: Predicts the price of a device based on its features using machine learning.
- **Device Recommendation**: Suggests devices that best match the user's requirements while adhering to their budget constraints.
- **Custom Python Package**: Includes a Python package published on PyPI, simplifying data analysis and preprocessing.
- **Budget-Aware Recommendations**: Considers user budget while ranking and recommending devices.

---

## Dataset

The dataset was webscraped from **Smartprix** using **Beautiful Soup** and saved in CSV format. It includes device features such as:

- Processor  
- RAM  
- Storage  
- Display  
- Battery  
- Price  
- Brand, and more.  

The data serves as the foundation for price prediction and recommendation tasks.
## Working

1. **Input Features**: Accepts user-provided specifications (e.g., processor, RAM, storage, etc.).
2. **Price Prediction**: Models trained on historical data predict device pricing.
3. **Recommendation Engine**: Finds the best-matching devices considering user preferences and budget.
   
## `pyprik`

PyPi LINK : https://pypi.org/project/pyprik/

<h2>Install the Package</h2>
<pre>
<code id="install-command" style="font-size: 55px;">pip install pyprik</code>
</pre>

<p align="center">
  <img src="Research/Screenshot 2024-12-01 144717.png" alt="Screenshot 1" >
</p>

Here’s how you can present the model performance and suggestions for improving accuracy in the README:

---

## Model Performance

Multiple regression models were used to predict device prices based on the provided features.

| **Model**             | **Training MSE** | **Testing MSE** | **Training R² Score** | **Testing R² Score** |
|------------------------|------------------|------------------|-----------------------|-----------------------|
| Linear Regression      | 2.171 × 10⁻³    | 1.677 × 10⁻³    | 0.7708               | 0.7911               |
| Decision Tree          | 1.230 × 10⁻³³   | 5.000 × 10⁻⁶    | 1.0000               | 0.9994               |
| Random Forest          | 2.602 × 10⁻⁶    | 5.000 × 10⁻⁶    | 0.9997               | 0.9994               |
| XGBoost                | 1.807 × 10⁻⁵    | 1.000 × 10⁻⁵    | 0.9981               | 0.9988               |

### Key Observations

- **Decision Tree** and **Random Forest** models provide nearly perfect performance with the lowest MSE and highest R² scores.
- **XGBoost** performs exceptionally well with minimal testing error and high accuracy.
- **Linear Regression** serves as a baseline model but performs relatively lower in accuracy.


## Git Clone and Run the App

1. **Clone the Repository**

2. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```


3. **Run the App**

    ```
    streamlit run app.py
    ```

