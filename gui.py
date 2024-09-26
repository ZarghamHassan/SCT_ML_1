import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('house_price_model.pkl')

def predict_sale_price():
    try:
        gr_liv_area = float(entry_gr_liv_area.get())
        bedroom_abv_gr = int(entry_bedroom_abv_gr.get())
        full_bath = int(entry_full_bath.get())
        
        # Create a DataFrame for the input features
        input_data = pd.DataFrame([[gr_liv_area, bedroom_abv_gr, full_bath]],
                                   columns=['GrLivArea', 'BedroomAbvGr', 'FullBath'])
        
        # Make prediction
        predicted_price = model.predict(input_data)
        
        # Display the result
        messagebox.showinfo("Prediction Result", f"The predicted sale price is: ${predicted_price[0]:,.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main application window
root = tk.Tk()
root.title("House Price Predictor")

# Create input fields
tk.Label(root, text="Ground Living Area (GrLivArea in sqft):").grid(row=0, column=0)
entry_gr_liv_area = tk.Entry(root)
entry_gr_liv_area.grid(row=0, column=1)

tk.Label(root, text="Bedrooms above grade (BedroomAbvGr):").grid(row=1, column=0)
entry_bedroom_abv_gr = tk.Entry(root)
entry_bedroom_abv_gr.grid(row=1, column=1)

tk.Label(root, text="Full Baths (FullBath):").grid(row=2, column=0)
entry_full_bath = tk.Entry(root)
entry_full_bath.grid(row=2, column=1)

# Create prediction button
predict_button = tk.Button(root, text="Predict Sale Price", command=predict_sale_price)
predict_button.grid(row=3, columnspan=2)

# Start the GUI event loop
root.mainloop()
