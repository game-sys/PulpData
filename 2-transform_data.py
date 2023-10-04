import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import seaborn as sns


# Specify the file path of the cleaned_data.csv file
file_path = 'pre_processed/cleaned_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Create a new DataFrame for the transformed data
transformed_df = pd.DataFrame()

# Iterate through unique IDs
for unique_id in df['UniqueID'].unique():
    patient_data = df[df['UniqueID'] == unique_id]

    # Create a new row for the patient
    new_row = {'UniqueID': unique_id}

    # Fill tooth-related columns for CEJ to Pulp horn (mm)
    for i in range(3, 9):
        mandible_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Mandible')]['CEJ to Pulp horn (mm)'].values
        maxilla_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Maxilla')]['CEJ to Pulp horn (mm)'].values
        new_row[f'CEJ to Pulp horn (mm)_tooth{i}_Mandible'] = mandible_value[0] if len(mandible_value) > 0 else 0
        new_row[f'CEJ to Pulp horn (mm)_tooth{i}_Maxilla'] = maxilla_value[0] if len(maxilla_value) > 0 else 0

    # Fill tooth-related columns for CEJ to cusp tip (mm)
    for i in range(3, 9):
        mandible_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Mandible')]['CEJ to cusp tip (mm)'].values
        maxilla_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Maxilla')]['CEJ to cusp tip (mm)'].values
        new_row[f'CEJ to cusp tip (mm)_tooth{i}_Mandible'] = mandible_value[0] if len(mandible_value) > 0 else 0
        new_row[f'CEJ to cusp tip (mm)_tooth{i}_Maxilla'] = maxilla_value[0] if len(maxilla_value) > 0 else 0

    # Fill tooth-related columns for Tooth-coronal index
    for i in range(3, 9):
        mandible_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Mandible')]['Tooth-coronal index'].values
        maxilla_value = patient_data[(patient_data['Tooth#'] == i) & (patient_data['Jaw'] == 'Maxilla')]['Tooth-coronal index'].values
        new_row[f'Tooth-coronal index_tooth{i}_Mandible'] = mandible_value[0] if len(mandible_value) > 0 else 0
        new_row[f'Tooth-coronal index_tooth{i}_Maxilla'] = maxilla_value[0] if len(maxilla_value) > 0 else 0

    # Fill Age and Gender
    new_row['Age'] = patient_data['Age'].iloc[0]
    new_row['Gender'] = patient_data['Gender'].iloc[0]

    # Append the new row to the transformed DataFrame
    transformed_df = transformed_df.append(new_row, ignore_index=True)


# Convert Gender to 1 for male and 0 for female
transformed_df["Gender"] = df["Gender"].apply(lambda x: 1 if x == "M" else 2)



# Count the number of individuals in each gender group
gender_counts = transformed_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Display the count of individuals in each gender group
print(gender_counts)



# List of column names to delete
columns_to_delete = ['CEJ to Pulp horn (mm)_tooth3_Mandible',
       'CEJ to Pulp horn (mm)_tooth3_Maxilla',
       'CEJ to Pulp horn (mm)_tooth4_Mandible',
       'CEJ to Pulp horn (mm)_tooth4_Maxilla',
       'CEJ to cusp tip (mm)_tooth3_Mandible',
       'CEJ to cusp tip (mm)_tooth3_Maxilla',
       'CEJ to cusp tip (mm)_tooth4_Mandible',
       'CEJ to cusp tip (mm)_tooth4_Maxilla',
       'Tooth-coronal index_tooth3_Mandible',
       'Tooth-coronal index_tooth3_Maxilla',
       'Tooth-coronal index_tooth4_Mandible',
       'Tooth-coronal index_tooth4_Maxilla',
       'CEJ to Pulp horn (mm)_tooth8_Maxilla',
       'CEJ to Pulp horn (mm)_tooth8_Mandible',
       'CEJ to cusp tip (mm)_tooth8_Mandible',
       'CEJ to cusp tip (mm)_tooth8_Maxilla',
       'Tooth-coronal index_tooth8_Mandible',
        'Tooth-coronal index_tooth8_Maxilla']

# Drop the specified columns from the DataFrame
transformed_df = transformed_df.drop(columns=columns_to_delete)

# Display the DataFrame after deleting the columns
print(transformed_df[:10])


# Save the transformed DataFrame to a CSV file
transformed_df.to_csv('pre_processed/transformed_data.csv', index=False)