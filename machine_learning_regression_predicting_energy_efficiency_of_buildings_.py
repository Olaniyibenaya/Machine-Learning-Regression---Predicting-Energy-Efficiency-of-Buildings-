# -*- coding: utf-8 -*-
"""Machine Learning: Regression - Predicting Energy Efficiency of Buildings .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vIOQHiFskFvL6jLcMVDfZzZBmbZwRj-r

### QUESTION 17
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv("/content/energydata_complete.csv")

# Select the features (independent variable) and target (dependent variable)
X = data[['T2']]
y = data['T6']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred

# Calculate the Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Print the RMSE rounded to 3 decimal places
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")

"""### QUESTION 18"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error

# Remove the specified columns
data = data.drop(["date", "lights"], axis=1)

# Define the features (independent variables) and the target (dependent variable)
X = data.drop("Appliances", axis=1)
y = data["Appliances"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the training set
y_pred_train = model.predict(X_train)

# Print the MAE rounded to 3 decimal places
print(f"Mean Absolute Error (MAE) for the training set: {mae_train:.3f}")

# Calculate the Mean Absolute Error (MAE) for the training set
mae_train = mean_absolute_error(y_train, y_pred_train)

print(f"Mean Absolute Error (MAE) for the training set: {mae_train:.3f}")

"""### QUESTION 19"""

# Calculate the Mean Squared Error (MSE) for the training set
mse_train = mean_squared_error(y_train, y_pred_train)

# Calculate the RMSE by taking the square root of the MSE
rmse_train = np.sqrt(mse_train)

print(f"Root Mean Squared Error (RMSE) for the training set: {rmse_train:.3f}")

"""### QUESTION 20"""

# Make predictions on the test set
y_pred_test = model.predict(X_test)

# Calculate the Mean Absolute Error (MAE) for the test set
mae_test = mean_absolute_error(y_test, y_pred_test)

# Print the MAE rounded to 3 decimal places
print(f"Mean Absolute Error (MAE) for the test set: {mae_test:.3f}")

"""### QUESTION 21"""

# Calculate the Mean Squared Error (MSE) for the test set
mse_test = mean_squared_error(y_test, y_pred_test)

#CAlculate the RMSE by taking the square root of the MSE
rmse_test = np.sqrt(mse_test)

# Print the RMSE rounded to 3 decimal places
print(f"Root Mean Squared Error (RMSE) for the test set: {rmse_test:.3f}")

"""### QUESTION 23"""

from sklearn.linear_model import Ridge

# Remove the specified columns
data = data.drop(["date", "lights"], axis=1)

# Define the features (independent variables) and the target (dependent variable)
X = data.drop("Appliances", axis=1)
y = data["Appliances"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler on the training data and transform both the training and testing data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and fit the Ridge regression model with default parameters
ridge_model = Ridge()
ridge_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_test = ridge_model.predict(X_test)

# Calculate the Mean Squared Error (MSE) for the test set
mse_test = mean_squared_error(y_test, y_pred_test)
# Calculate the RMSE by taking the square root of the MSE
rmse_test = np.sqrt(mse_test)

# Print the RMSE rounded to 3 decimal places
print(f"Root Mean Squared Error (RMSE) for the test set with Ridge regression: {rmse_test:.3f}")

