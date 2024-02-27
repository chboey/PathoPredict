import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Load the test dataset
test_data = pd.read_excel("TestDatasetExample.xls", header=None, na_values=['?'])

# Assume the first row contains column names
test_data.columns = test_data.iloc[0]
test_data = test_data.iloc[1:]

# Extract the 'ID' column
test_ids = test_data['ID']

# Extract selected feature from implementation
selected_features = ['ER', 'PgR', 'HER2', 'LNStatus', 'original_firstorder_10Percentile',
                     'original_gldm_DependenceEntropy',
                     'original_gldm_LargeDependenceEmphasis',
                     'original_glrlm_RunLengthNonUniformityNormalized',
                     'original_glrlm_RunPercentage']

test_data = test_data[selected_features]

# Exclude non-numeric columns from scaling (assuming 'ID' is non-numeric)
non_numeric_columns = ['ID']
numeric_columns = [col for col in test_data.columns if col not in non_numeric_columns]

# Replace 999 with NaN in numeric columns
test_data[numeric_columns] = test_data[numeric_columns].replace(999, np.nan)

# Mean imputation for numeric columns
test_data_imputed = test_data.copy()
test_data_imputed[numeric_columns] = test_data_imputed[numeric_columns].fillna(
    test_data_imputed[numeric_columns].mean())

# Standardize only numeric columns
scaler = StandardScaler()
test_data_standardized = test_data_imputed.copy()
test_data_standardized[numeric_columns] = scaler.fit_transform(test_data_imputed[numeric_columns])

# Load the model
loaded_model = joblib.load('AdaBoost_Model.joblib')

# Predict using each model
predictions = pd.DataFrame({"ID": test_ids})

PCR_pred = loaded_model.predict(test_data_standardized[numeric_columns])
predictions["pCR( outcome )"] = PCR_pred

# Save predictions to a CSV file
predictions.to_csv("FinalTestPCR.csv", index=False)
