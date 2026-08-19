# 🏠 House Price Prediction using Scikit-learn

A machine learning project that predicts house prices using **Linear Regression** and a complete **Scikit-learn pipeline**.

## 📌 Project Overview

The objective of this project is to predict house prices based on different property features such as area, bedrooms, bathrooms, stories, parking, and other house characteristics.

The project follows a complete machine learning workflow, from data understanding and EDA to preprocessing, model training, evaluation, cross-validation, and user-input prediction.

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## 📊 Dataset

- **Rows:** 545
- **Features:** 12
- **Target:** `price`

### Features

- `area`
- `bedrooms`
- `bathrooms`
- `stories`
- `mainroad`
- `guestroom`
- `basement`
- `hotwaterheating`
- `airconditioning`
- `parking`
- `prefarea`
- `furnishingstatus`

## 🔄 Machine Learning Workflow

```text
Data Understanding
        ↓
Exploratory Data Analysis
        ↓
Train/Test Split
        ↓
Missing Value Handling
        ↓
Categorical Encoding
        ↓
Feature Scaling
        ↓
ColumnTransformer
        ↓
Pipeline
        ↓
Linear Regression
        ↓
Cross-Validation
        ↓
Model Evaluation
        ↓
User Input Prediction
