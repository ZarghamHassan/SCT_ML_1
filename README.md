# House Price Prediction

## Overview

This project implements a machine learning model to predict house prices based on features such as ground living area, number of bedrooms above grade, and the number of full baths. A Linear Regression model is trained on historical data to provide accurate price predictions. The project includes a user-friendly GUI for easy interaction.

## Features

- **Linear Regression Model**: Predicts house prices using a trained Linear Regression model.
- **User-Friendly GUI**: Allows users to input property features and receive instant predictions.
- **Model Saving**: The trained model is saved for reuse without needing to retrain.
- **Input Validation**: Ensures that users enter valid numeric values for prediction.

## Model

This project utilizes a **Linear Regression** model from the `scikit-learn` library to predict house prices based on input features. The model is trained on historical housing data and saved as `house_prediction_model.pkl` for future predictions.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Tkinter

## Dataset

The model is trained using a dataset that includes the following columns:
- `GrLivArea`: Ground Living Area (in sqft)
- `BedroomAbvGr`: Number of Bedrooms above grade
- `FullBath`: Number of Full Baths
- `SalePrice`: Sale Price of the house (target variable)

### Obtaining the Dataset
You can download the dataset from [Kaggle: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data). Please ensure that you have the required columns as mentioned above in the training CSV file (`train.csv`) and the testing CSV file (`test.csv`).

## Requirements

To run this project, you will need the following libraries:

- pandas
- scikit-learn
- joblib
- tkinter (usually included with Python installations)

You can install the required libraries using pip:

```bash
pip install pandas scikit-learn joblib
```
## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd house-price-prediction
   ```
2. **Prepare Your Data**:
    Ensure that you have the training dataset (`train.csv`) and the testing dataset (`test.csv`) in the root directory of the project.
3. **Train the Model**: Run the following script to train the model and save it:
   ```bash
   python House Prediction Model.py
   ```
4. **Use the Predictor**: The trained model can be used programmatically through the predictor file (`predictor.py`). You can input the features directly in this script to receive predictions.
   ```bash
   python Predictor.py
   ```
5. **Run the GUI**: Execute the following script to open the GUI:
   ```bash
   python gui.py
   ```
## Usage

To use the application:

- **Input Features**: 
  - Enter the Ground Living Area (in sqft).
  - Enter the number of Bedrooms above grade.
  - Enter the number of Full Baths.

- **Make Prediction**: 
  - Click the "Predict Sale Price" button to see the predicted sale price displayed in a popup.
