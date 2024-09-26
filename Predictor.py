import pandas as pd
import joblib

# Load the saved model
model = joblib.load('house_price_model.pkl')

def predict_sale_price(gr_liv_area, bedroom_abv_gr, full_bath):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame([[gr_liv_area, bedroom_abv_gr, full_bath]],
                               columns=['GrLivArea', 'BedroomAbvGr', 'FullBath'])
    
    # Make prediction
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Example usage: Input new data
try:
    gr_liv_area = float(input("Enter the Ground Living Area (GrLivArea) in sqft: "))
    bedroom_abv_gr = int(input("Enter the number of Bedrooms above grade (BedroomAbvGr): "))
    full_bath = int(input("Enter the number of Full Baths (FullBath): "))
    
    predicted_price = predict_sale_price(gr_liv_area, bedroom_abv_gr, full_bath)
    print(f"The predicted sale price is: ${predicted_price:,.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
