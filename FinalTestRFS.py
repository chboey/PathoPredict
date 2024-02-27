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
selected_features = ['ChemoGrade', 'TumourStage', 'original_shape_LeastAxisLength',
                     'original_shape_MajorAxisLength',
                     'original_shape_Maximum2DDiameterColumn',
                     'original_shape_Maximum2DDiameterRow',
                     'original_shape_Maximum2DDiameterSlice',
                     'original_shape_Maximum3DDiameter', 'original_shape_MinorAxisLength',
                     'original_shape_Sphericity', 'original_firstorder_90Percentile',
                     'original_firstorder_InterquartileRange',
                     'original_firstorder_Kurtosis', 'original_firstorder_Maximum',
                     'original_firstorder_MeanAbsoluteDeviation',
                     'original_firstorder_Range',
                     'original_firstorder_RobustMeanAbsoluteDeviation',
                     'original_firstorder_RootMeanSquared', 'original_firstorder_Variance',
                     'original_glszm_ZoneEntropy', 'original_glszm_ZonePercentage']

test_data = test_data[selected_features]

# Exclude non-numeric columns from scaling (assuming 'ID' is non-numeric)
non_numeric_columns = ['ID']
numeric_columns = [col for col in test_data.columns if col not in non_numeric_columns]

# Replace 999 with NaN in numeric columns
test_data[numeric_columns] = test_data[numeric_columns].replace(999, np.nan)

# Mean imputation for numeric columns
test_data_imputed = test_data.copy()
test_data_imputed[numeric_columns] = test_data_imputed[numeric_columns].fillna(
    test_data_imputed[numeric_columns].median())

# Standardize only numeric columns
scaler = StandardScaler()
test_data_standardized = test_data_imputed.copy()
test_data_standardized[numeric_columns] = scaler.fit_transform(test_data_imputed[numeric_columns])

# Load the model
loaded_model = joblib.load('RandomForest_Regressor_Model.joblib')

# Predict using each model
predictions = pd.DataFrame({"ID": test_ids})

RFS_pred = loaded_model.predict(test_data_standardized[numeric_columns])
predictions["RelapseFreeSurvival (outcome)"] = RFS_pred

# Save predictions to a CSV file
predictions.to_csv("FinalTestRFS.csv", index=False)
