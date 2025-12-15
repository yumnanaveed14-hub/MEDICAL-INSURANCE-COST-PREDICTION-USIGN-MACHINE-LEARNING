# Medical Insurance Cost Prediction using Machine Learning
Machine learning project to predict medical insurance costs using regression models of Linear Regression and Random Forest with Gradio, Flask, and Fast API deployment.

# Project Overview
This project focuses on predicting medical insurance costs using machine learning techniques. 
The goal is to analyze different factors such as age, BMI, smoking habits, and region, and predict the insurance charges for an individual.

# Objectives
- To understand how machine learning can be used for cost prediction
- To analyze factors affecting medical insurance charges
- To build and compare regression-based ML models
- To deploy the trained model using different interfaces

# Dataset
- Source: Kaggle (Medical Insurance Dataset)
- Features used:
  - Age
  - Sex
  - BMI
  - Children
  - Smoker
  - Region
- Target variable:
  - Insurance Charges
The dataset was preprocessed by encoding categorical variables and handling basic data cleaning.

# Methodology
1. Data loading and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Model training using:
   - Linear Regression   
   - Random Forest Regressor  
4. Model evaluation using performance metrics  
5. Selection of the best-performing model  
6. Deployment using user interfaces and APIs  

# Technologies Used
- Python
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn
- Gradio (User Interface)
- Flask (REST API)
- FastAPI (REST API)
- Joblib
- Jupyter Notebook

# User Interfaces & Deployment
- **Gradio Interface**: Allows users to enter values and get predictions easily
- **Flask API**: Backend REST API for prediction
- **FastAPI**: Modern API framework with automatic documentation

# Results
 Random Forest model performed better compared to basic linear regression, showing improved accuracy due to non-linear relationships in the data.


# Conclusion
Machine learning models can effectively predict medical insurance costs when relevant features are used. 
This project demonstrates the complete ML pipeline from data collection to deployment.
