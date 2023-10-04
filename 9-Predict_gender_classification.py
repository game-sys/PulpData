import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix, classification_report
import joblib

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
# Replace 0.0 with the mean of the respective column
tooth5_df = tooth5_df.replace(0.0, column_means)

# Calculate the mean of each column
column_means = tooth6_df.median()
# Replace 0.0 with the mean of the respective column
tooth6_df = tooth6_df.replace(0.0, column_means)

# Calculate the mean of each column
column_means = tooth7_df.median()
# Replace 0.0 with the mean of the respective column
tooth7_df = tooth7_df.replace(0.0, column_means)

# Separate the target variable (y) and features (X) for tooth5 dataset
y_tooth5 = tooth5_df["Gender"]
X_tooth5 = tooth5_df.drop(columns=["AgeGroup","Gender"])

# Split the data into training and testing sets (80% train, 20% test)
X_train_tooth5, X_test_tooth5, y_train_tooth5, y_test_tooth5 = train_test_split(X_tooth5, y_tooth5, test_size=0.2, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth5 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth5, y_train_resampled_tooth5 = smote_tooth5.fit_resample(X_train_tooth5, y_train_tooth5)

# Print the shapes of the train and test sets for tooth5 dataset
print("X_train tooth5 shape:", X_train_resampled_tooth5.shape)
print("X_test tooth5 shape:", X_test_tooth5.shape)
print("y_train tooth5 shape:", y_train_resampled_tooth5.shape)
print("y_test tooth5 shape:", y_test_tooth5.shape)


# Separate the target variable (y) and features (X) for tooth6 dataset
y_tooth6 = tooth6_df["Gender"]
X_tooth6 = tooth6_df.drop(columns=["AgeGroup","Gender"])

# Split the data into training and testing sets (80% train, 20% test)
X_train_tooth6, X_test_tooth6, y_train_tooth6, y_test_tooth6 = train_test_split(X_tooth6, y_tooth6, test_size=0.2, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth6 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth6, y_train_resampled_tooth6 = smote_tooth6.fit_resample(X_train_tooth6, y_train_tooth6)

# Print the shapes of the train and test sets for tooth6 dataset
print("X_train tooth6 shape:", X_train_resampled_tooth6.shape)
print("X_test tooth6 shape:", X_test_tooth6.shape)
print("y_train tooth6 shape:", y_train_resampled_tooth6.shape)
print("y_test tooth6 shape:", y_test_tooth6.shape)


# Separate the target variable (y) and features (X) for tooth7 dataset
y_tooth7 = tooth7_df["Gender"]
X_tooth7 = tooth7_df.drop(columns=["AgeGroup","Gender"])

# Split the data into training and testing sets (80% train, 20% test)
X_train_tooth7, X_test_tooth7, y_train_tooth7, y_test_tooth7 = train_test_split(X_tooth7, y_tooth7, test_size=0.2, random_state=42)

# Apply SMOTE to oversample the minority class
smote_tooth7 = SMOTE(sampling_strategy='auto', random_state=42)
X_train_resampled_tooth7, y_train_resampled_tooth7 = smote_tooth7.fit_resample(X_train_tooth7, y_train_tooth7)

# Print the shapes of the train and test sets for tooth7 dataset
print("X_train tooth7 shape:", X_train_resampled_tooth7.shape)
print("X_test tooth7 shape:", X_test_tooth7.shape)
print("y_train tooth7 shape:", y_train_resampled_tooth7.shape)
print("y_test tooth7 shape:", y_test_tooth7.shape)

# Load the saved models
loaded_rf_tooth5 = joblib.load('pre_processed/best_rf_tooth5_gender_model.pkl')
loaded_rf_tooth6 = joblib.load('pre_processed/best_rf_tooth6_gender_model.pkl')
loaded_rf_tooth7 = joblib.load('pre_processed/best_rf_tooth7_gender_model.pkl')


# Make predictions on the test data for tooth5
y_pred_rf_tooth5_1 = loaded_rf_tooth5.predict(X_test_tooth5)
y_pred_rf_tooth5_2 = loaded_rf_tooth6.predict(X_test_tooth6)
y_pred_rf_tooth5_3 = loaded_rf_tooth7.predict(X_test_tooth7)


# Combine the predictions into a single DataFrame or array
ensemble_predictions = pd.DataFrame({
    'tooth5': y_pred_rf_tooth5_1,
    'tooth6': y_pred_rf_tooth5_2,
    'tooth7': y_pred_rf_tooth5_3
})

# Calculate the majority vote for each sample
majority_vote = ensemble_predictions.mode(axis=1).iloc[:, 0]

# Assign the majority vote as the final prediction
final_predictions = majority_vote.values


# Evaluate the models for tooth5
accuracy_rf_tooth5_1 = accuracy_score(y_test_tooth5, y_pred_rf_tooth5_1)
accuracy_rf_tooth5_2 = accuracy_score(y_test_tooth6, y_pred_rf_tooth5_2)
accuracy_rf_tooth5_3 = accuracy_score(y_test_tooth7, y_pred_rf_tooth5_3)
accuracy_rf_final=accuracy_score(y_test_tooth7,final_predictions)

# Print the accuracy of each model for tooth5
print("Random Forest Accuracy 1 (tooth5):", accuracy_rf_tooth5_1)
print("Random Forest Accuracy 2 (tooth6):", accuracy_rf_tooth5_2)
print("Random Forest Accuracy 3 (tooth7):", accuracy_rf_tooth5_3)

print("Random Forest Ensembele Accuracy final:", accuracy_rf_final)
