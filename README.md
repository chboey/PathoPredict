# Predictive Modelling of Pathological Complete Response and Relapse-Free Survival in Cancer Patients

## Overview
This repository contains the implementation of a machine learning project aimed at enhancing the accuracy of predicting Pathological Complete Response (PCR) and Relapse-Free Survival (RFS) in chemotherapy-treated breast cancer patients. The project analyzes a dataset with clinical and MRI features across 400 patients to provide additional prognosis information for personalized treatment recommendations.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methods](#methods)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Selection](#model-selection)
  - [Model Evaluation](#model-evaluation)
- [Results](#results)
  - [Classification Results](#classification-results)
  - [Regression Results](#regression-results)
- [Conclusion](#conclusion)
- [References](#references)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to improve the predictions of PCR and RFS in breast cancer patients using various machine learning techniques. Accurate predictions can guide treatment decisions and provide better prognostic information.

## Dataset
The dataset used in this project is publicly available from The American College of Radiology Imaging Network. It includes:
- 10 clinical features
- 107 MRI-based features
- 400 patient records

## Methods

### Data Preprocessing
- **Handling Missing Values**: Rows with missing values denoted by '999' were removed. Median imputation was used for remaining missing values.
- **Feature Selection**: ANOVA was used to assess the importance of each feature. Features with an f-score above 3.5 were selected.

### Model Selection

#### Classification Models
- **Logistic Regression**
- **AdaBoost Classifier**
- **Support Vector Machine (SVM)**
- **Voting Classifier**

#### Regression Models
- **Random Forest Regressor**
- **Support Vector Regressor (SVR)**
- **LASSO Regressor**
- **Ridge Regressor**
- **AdaBoost Regressor**

### Model Evaluation
- **Classification Metrics**: Balanced Accuracy, Precision
- **Regression Metrics**: Mean Absolute Error (MAE)
- **Hyperparameter Tuning**: Grid Search

## Results

### Classification Results
- **AdaBoost Classifier**: Balanced Accuracy - 73.43%, Precision - 70.59%
- **Voting Classifier**: Balanced Accuracy - 70.68%, Precision - 83.33%

### Regression Results
- **Random Forest Regressor**: MAE - 20.43
- **LASSO Regressor**: MAE - 20.84

## Conclusion
The AdaBoost Classifier was the best model for predicting PCR due to its balanced accuracy and precision. The Random Forest Regressor was the most effective for predicting RFS with the lowest MAE and robust performance.

## References
- Dhillon, A., & Singh, A. (2020). eBreCaP: extreme learning-based model for breast cancer survival prediction. IET Systems Biology, 14(3), 160–169.
- Tahmassebi, A., et al. (2019). Impact of Machine Learning With Multiparametric MRI for Early Prediction of Response to Neoadjuvant Chemotherapy and Survival Outcomes in Breast Cancer Patients. Investigative Radiology, 54(2), 110–117.
- Tapak, L., et al. (2019). Prediction of survival and metastasis in breast cancer patients using machine learning classifiers. Clinical Epidemiology and Global Health, 7(3), 293–299.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/breast-cancer-prediction.git
