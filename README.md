# Predictive Modelling of Pathological Complete Response and Relapse-Free Survival in Cancer Patients

## Overview
This repository contains the implementation of a machine learning project aimed at enhancing the accuracy of predicting Pathological Complete Response (PCR) and Relapse-Free Survival (RFS) in chemotherapy-treated breast cancer patients. The project analyzes a dataset with clinical and MRI features across 400 patients to provide additional prognosis information for personalized treatment recommendations.

## Introduction
This project aims to improve the predictions of PCR and RFS in breast cancer patients using various machine learning techniques. Accurate predictions can guide treatment decisions and provide better prognostic information.

## Dataset
The dataset used in this project is publicly available from The American College of Radiology Imaging Network.

| Feature Type | Number of Features |
|--------------|--------------------|
| Clinical     | 10                 |
| MRI-based    | 107                |
| Total Records| 400                |

## Methods

### Data Preprocessing
- **Handling Missing Values**: Rows with missing values denoted by '999' were removed. Median imputation was used for remaining missing values.
- **Feature Selection**: ANOVA was used to assess the importance of each feature. Features with an f-score above 3.5 were selected.

### Model Selection

| Model Type      | Model                         |
|-----------------|-------------------------------|
| Classification  | Logistic Regression           |
|                 | AdaBoost Classifier           |
|                 | Support Vector Machine (SVM)  |
|                 | Voting Classifier             |

| Model Type      | Model                         |
| Regression      | Random Forest Regressor       |
|                 | Support Vector Regressor (SVR)|
|                 | LASSO Regressor               |
|                 | Ridge Regressor               |
|                 | AdaBoost Regressor            |

### Model Evaluation

| Evaluation Type | Metric                     |
|-----------------|----------------------------|
| Classification  | Balanced Accuracy          |
|                 | Precision                  |
| Regression      | Mean Absolute Error (MAE)  |
| Tuning          | Grid Search                |

## Results

### Classification Results

| Model                 | Balanced Accuracy | Precision |
|-----------------------|-------------------|-----------|
| AdaBoost Classifier   | 73.43%            | 70.59%    |
| Voting Classifier     | 70.68%            | 83.33%    |

### Regression Results

| Model                  | Mean Absolute Error (MAE) |
|------------------------|---------------------------|
| Random Forest Regressor| 20.43                     |
| LASSO Regressor        | 20.84                     |


## Conclusion
The AdaBoost Classifier was the best model for predicting PCR due to its balanced accuracy and precision. The Random Forest Regressor was the most effective for predicting RFS with the lowest MAE and robust performance.
