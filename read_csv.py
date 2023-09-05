import pandas as pd
# Display all columns
pd.set_option('display.max_columns', None)
# Replace 'data\Bitewings_results.xlsx' with the actual file path
file_path = 'data\Bitewings_results.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)
# Drop the 'Set' and 'File name' columns
df = df.drop(['Set', 'File name', 'S.N'], axis=1)

print(df[:10])

# Get the total number of rows
total_rows = df.shape[0]

# Display the total number of rows
print(f'Total rows in the DataFrame: {total_rows}')

# Display unique values in the 'Tooth#' column
unique_tooth_values = df['Tooth#'].unique()
print(f'Unique tooth numbers in Tooth# column:{unique_tooth_values}')

# Display unique values in the 'Jaw' column
unique_jaw_values = df['Jaw'].unique()
print(f'Unique values in Jaw column: {unique_jaw_values}')

# Group by 'Tooth#' and 'Jaw', and then count the occurrences
tooth_jaw_counts = df.groupby(['Tooth#', 'Jaw']).size().reset_index(name='Count')

# Display the counts for each tooth and jaw combination
print(tooth_jaw_counts)

# Group the DataFrame by 'Tooth#' and 'Jaw'
grouped = df.groupby(['Tooth#', 'Jaw'])

# Iterate through each group and save it to a CSV file
for name, group in grouped:
    tooth, jaw = name
    filename = f'tooth{tooth}{jaw}.csv'
    group.to_csv(filename, index=False)
    print(f'Saved {filename}')

print('done')