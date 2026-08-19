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

## ⚙️ Preprocessing
Numerical Features
Missing values → Median Imputation
Feature scaling → StandardScaler
Categorical Features
Missing values → Most Frequent Imputation
Encoding → OneHotEncoder

All preprocessing and model training are combined using a Scikit-learn Pipeline.

🤖 Model

Linear Regression

The model is trained using Scikit-learn's LinearRegression.

📈 Model Performance
Metric	Score
MAE	962,528.89
RMSE	1,321,857.16
R² Score	0.6543
Mean CV R²	0.6383

The model achieved an R² score of 0.6543 on the test set.

R² is used as the evaluation metric here; it should not be interpreted as model accuracy.

🔮 User Input Prediction

The trained pipeline can predict house prices based on user-provided property details.

Example inputs include:

Area
Bedrooms
Bathrooms
Stories
Parking
Mainroad
Guestroom
Basement
Hot Water Heating
Air Conditioning
Preferred Area
Furnishing Status

The complete preprocessing pipeline is automatically applied to new user input before generating the prediction.

📁 Project Structure
house-price-scikit-learn/
│
├── data/
│   └── Housing.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   └── predict.py
│
├── images/
│   ├── price_distribution.png
│   ├── correlation_matrix.png
│   ├── categorical_features.png
│   ├── residual_plot.png
│   └── actual_vs_predicted.png
│
├── models/
│   └── house_price_model.pkl
│
├── requirements.txt
├── .gitignore
└── README.md
🚀 Future Improvements
Compare multiple regression algorithms
Hyperparameter tuning
Improve model performance
Deploy the model using Streamlit
👨‍💻 Author

Sahil Bhayre



### One correction I intentionally made


Don't write:


> **Accuracy: 65.43%**


for this project.


Your **R² = 0.6543**, so write **R² Score: 0.6543**. That's technically correct and looks m
