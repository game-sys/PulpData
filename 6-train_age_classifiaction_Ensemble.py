import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib
from sklearn.model_selection import GridSearchCV

# Specify the file paths for the three CSV files
tooth5_file_path = "pre_processed/tooth5_data.csv"
tooth6_file_path = "pre_processed/tooth6_data.csv"
tooth7_file_path = "pre_processed/tooth7_data.csv"

# Read each CSV file into a separate DataFrame
tooth5_df = pd.read_csv(tooth5_file_path)
tooth6_df = pd.read_csv(tooth6_file_path)
tooth7_df = pd.read_csv(tooth7_file_path)

# Calculate the mean of each column
column_means = tooth5_df.median()
tooth5_df = tooth5_df.replace(0.0, column_means)

# Calculate the mean of each column
column_means = tooth6_df.median()
tooth6_df = tooth6_df.replace(0.0, column_means)

# Calculate the mean of each column
column_means = tooth7_df.median()
tooth7_df = tooth7_df.replace(0.0, column_means)


# Separate the target variable (y) and features (X) for tooth5 dataset
y_tooth5 = tooth5_df["AgeGroup"]
X_tooth5 = tooth5_df.drop(columns=["AgeGroup","Gender"])


X_train_tooth5, X_test_tooth5, y_train_tooth5, y_test_tooth5 = train_test_split(X_tooth5, y_tooth5, test_size=0.1, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth5 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth5, y_train_resampled_tooth5 = smote_tooth5.fit_resample(X_train_tooth5, y_train_tooth5)


# Separate the target variable (y) and features (X) for tooth6 dataset
y_tooth6 = tooth6_df["AgeGroup"]
X_tooth6 = tooth6_df.drop(columns=["AgeGroup","Gender"])


X_train_tooth6, X_test_tooth6, y_train_tooth6, y_test_tooth6 = train_test_split(X_tooth6, y_tooth6, test_size=0.1, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth6 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth6, y_train_resampled_tooth6 = smote_tooth6.fit_resample(X_train_tooth6, y_train_tooth6)


# Separate the target variable (y) and features (X) for tooth7 dataset
y_tooth7 = tooth7_df["AgeGroup"]
X_tooth7 = tooth7_df.drop(columns=["AgeGroup","Gender"])


X_train_tooth7, X_test_tooth7, y_train_tooth7, y_test_tooth7 = train_test_split(X_tooth7, y_tooth7, test_size=0.1, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth7 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth7, y_train_resampled_tooth7 = smote_tooth7.fit_resample(X_train_tooth7, y_train_tooth7)


# Define the hyperparameters to search
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf = RandomForestClassifier()

# Perform Grid Search Cross-Validation
grid_search_tooth5 = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search_tooth5.fit(X_train_resampled_tooth5, y_train_resampled_tooth5)

# Get the best parameters
best_params_tooth5 = grid_search_tooth5.best_params_


# Perform Grid Search Cross-Validation
grid_search_tooth6 = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search_tooth6.fit(X_train_resampled_tooth6, y_train_resampled_tooth6)

# Get the best parameters
best_params_tooth6 = grid_search_tooth6.best_params_

# Perform Grid Search Cross-Validation
grid_search_tooth7 = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search_tooth7.fit(X_train_resampled_tooth7, y_train_resampled_tooth7)

# Get the best parameters
best_params_tooth7 = grid_search_tooth7.best_params_

# Train a Random Forest classifier with the best parameters
best_rf_tooth5 = RandomForestClassifier(**best_params_tooth5)
best_rf_tooth6 = RandomForestClassifier(**best_params_tooth6)
best_rf_tooth7 = RandomForestClassifier(**best_params_tooth7)

# Train the Random Forest classifiers on the resampled training data for tooth5
best_rf_tooth5.fit(X_train_resampled_tooth5, y_train_resampled_tooth5)
best_rf_tooth6.fit(X_train_resampled_tooth6, y_train_resampled_tooth6)
best_rf_tooth7.fit(X_train_resampled_tooth7, y_train_resampled_tooth7)
# Define file paths to save the models
model_file_path_tooth5 = "pre_processed/best_rf_tooth5_age_model.pkl"
model_file_path_tooth6 = "pre_processed/best_rf_tooth6_age_model.pkl"
model_file_path_tooth7 = "pre_processed/best_rf_tooth7_age_model.pkl"

# Save the models to the specified file paths
joblib.dump(best_rf_tooth5, model_file_path_tooth5)
joblib.dump(best_rf_tooth6, model_file_path_tooth6)
joblib.dump(best_rf_tooth7, model_file_path_tooth7)

print("Models saved successfully.")

