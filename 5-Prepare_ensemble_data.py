import pandas as pd

# Specify the file path
file_path = "pre_processed/transformed_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the mean of each column
column_means = df.median()

# Replace 0.0 with the mean of the respective column
df = df.replace(0.0, column_means)

print(df[:10])

# Assuming you already have a DataFrame named 'df'
column_names = df.columns

# Print the names of each column
for column_name in column_names:
    print(column_name)


# Define the age groups and corresponding labels
age_groups = {
    1: (0, 21),
    2: (21, 31),
    3: (31, 41),
    4: (41, 51),
    5: (51, float('inf'))
}

# Function to map age to age group
def map_age_to_group(age):
    for group, (min_age, max_age) in age_groups.items():
        if min_age <= age < max_age:
            return group
    return None

# Apply the mapping function to the 'Age' column and create a new 'AgeGroup' column
df['AgeGroup'] = df['Age'].apply(map_age_to_group)

# Drop the original 'Age' column
transformed_df = df.drop(['Age'], axis=1)

# Function to map age to age group
def map_age_to_group(age):
    for group, (min_age, max_age) in age_groups.items():
        if min_age <= age < max_age:
            return group
    return None



# Count the number of individuals in each age group
age_group_counts = transformed_df['AgeGroup'].value_counts().reset_index()
age_group_counts.columns = ['AgeGroup', 'Count']

# Display the count of individuals in each age group
print(age_group_counts)

# Specify the columns you want to save
columns_to_save = [
    'CEJ to Pulp horn (mm)_tooth5_Mandible',
    'CEJ to Pulp horn (mm)_tooth5_Maxilla',
    'CEJ to cusp tip (mm)_tooth5_Mandible',
    'CEJ to cusp tip (mm)_tooth5_Maxilla',
    'Tooth-coronal index_tooth5_Mandible',
    'Tooth-coronal index_tooth5_Maxilla',
    'AgeGroup','Gender'
]

# Create a new DataFrame with the selected columns
selected_columns_df = df[columns_to_save]

# Specify the file path where you want to save the data
save_path = "pre_processed/tooth5_data.csv"

# Save the selected columns to a CSV file
selected_columns_df.to_csv(save_path, index=False)


# Specify the columns you want to save
columns_to_save = [
    'CEJ to Pulp horn (mm)_tooth6_Mandible',
    'CEJ to Pulp horn (mm)_tooth6_Maxilla',
    'CEJ to cusp tip (mm)_tooth6_Mandible',
    'CEJ to cusp tip (mm)_tooth6_Maxilla',
    'Tooth-coronal index_tooth6_Mandible',
    'Tooth-coronal index_tooth6_Maxilla',
    'AgeGroup','Gender'
]

# Create a new DataFrame with the selected columns
selected_columns_df = df[columns_to_save]

# Specify the file path where you want to save the data
save_path = "pre_processed/tooth6_data.csv"

# Save the selected columns to a CSV file
selected_columns_df.to_csv(save_path, index=False)



# Specify the columns you want to save
columns_to_save = [
    'CEJ to Pulp horn (mm)_tooth7_Mandible',
    'CEJ to Pulp horn (mm)_tooth7_Maxilla',
    'CEJ to cusp tip (mm)_tooth7_Mandible',
    'CEJ to cusp tip (mm)_tooth7_Maxilla',
    'Tooth-coronal index_tooth7_Mandible',
    'Tooth-coronal index_tooth7_Maxilla',
    'AgeGroup','Gender'
]

# Create a new DataFrame with the selected columns
selected_columns_df = df[columns_to_save]

# Specify the file path where you want to save the data
save_path = "pre_processed/tooth7_data.csv"

# Save the selected columns to a CSV file
selected_columns_df.to_csv(save_path, index=False)

