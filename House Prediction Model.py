# 1. Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 2. Load the training and test datasets (keeping only necessary columns)
train_data = pd.read_csv('train.csv', usecols=['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice'])
test_data = pd.read_csv('test.csv', usecols=['GrLivArea', 'BedroomAbvGr', 'FullBath'])
print(train_data.head)
# 3. Prepare the data
X_train = train_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]  # Features for training
y_train = train_data['SalePrice']  # Target: Sale price

X_test = test_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]  # Features for testing

# 4. Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model on the training set
y_train_pred = model.predict(X_train)

# Calculate metrics on the training set
mse = mean_squared_error(y_train, y_train_pred)
rmse = mse ** 0.5
r2 = r2_score(y_train, y_train_pred)

print(f"Training Set Performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.4f}")

# 6. Save the trained model to a file
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as 'house_price_model.pkl'")

# 7. Make predictions on the test set (without actual 'SalePrice' in the test set)
y_test_pred = model.predict(X_test)

# 8. Output the predictions for the test set
test_data['PredictedSalePrice'] = y_test_pred
test_data.to_csv('test_with_predictions.csv', index=False)  # Save predictions to a new CSV file

print("Predictions saved to 'test_with_predictions.csv'")
