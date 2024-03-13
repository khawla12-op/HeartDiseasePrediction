
# Heart Disease Prediction 

## Introduction
This project aims to address the critical task of disease diagnosis within the medical system, with a focus on swiftly predicting heart disease. The current challenge lies in the rapid and accurate prediction of heart disease, as delays in diagnosis contribute to escalating mortality rates. Thus, the development of a web-based automatic prediction system becomes imperative to reduce mortality rates by providing timely diagnosis and intervention.

### Problem Statement
The primary challenge is to develop a system that can automatically predict heart disease based on various health parameters. This involves solving a binary classification problem using supervised machine learning techniques.

### Objectives
The main objectives of this project are as follows:
1. Development of a web-based automatic prediction system.
2. Integration of predictive algorithms to accurately forecast heart disease.
3. Designing user-friendly interfaces for healthcare professionals and patients.

### Scope
The scope of this project includes the following tasks:
1. Development of a Web-Based Automatic Prediction System: Design and implementation of a web-based platform capable of automatically predicting heart disease based on input parameters.
2. Integration of Predictive Algorithms: Incorporation of machine learning algorithms to analyze health parameters such as blood pressure, cholesterol levels, etc., to predict the likelihood of heart disease.
3. User Interface Design: Creation of intuitive and user-friendly interfaces for both healthcare professionals and patients to input data and interpret results effectively.

## Data Collection and Preprocessing

### Data Sourcing
The data used for this project was sourced from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease).

### Data Cleaning
The dataset contained missing values in the 'ca' and 'thal' columns. We handled these missing values by replacing them with the mean and dropping rows with missing values.

### Splitting the Dataset
We split the dataset into training and testing sets to ensure the effectiveness of our model and to avoid overfitting.

## Algorithm Selection
We explored several machine learning algorithms commonly used for classification tasks to select the optimal model for our dataset. Here are some of the algorithms we considered:

- K-Nearest Neighbors (KNN)
- AdaBoost Classifier
- Logistic Regression
- Support Vector Machine (SVM)

## Evaluation of our Model
We selected various metrics such as overall accuracy, precision, recall, and F1-score to evaluate the performance of our model using a confusion matrix.

### Metrics Selection
The confusion matrix provides a clear breakdown of the model's performance in terms of correctly classified data points.

Benefits of Using a Confusion Matrix:
- Visualization
- Identification of Errors
- Evaluation and Comparison

