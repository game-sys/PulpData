import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import seaborn as sns


# Display all columns
pd.set_option('display.max_columns', None)

file_path = 'data/Bitewings_results.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)
# Drop the 'Set' and 'File name' columns
df = df.drop(['File name'], axis=1)

# Create a new column 'UniqueID' by combining 'Set' and 'S.N'
df['UniqueID'] = df['Set'] + '_' + df['S.N'].astype(str)

# Drop the 'Set' and 'S.N' columns
df = df.drop(['Set', 'S.N'], axis=1)

# Rearrange the columns with 'UniqueID' at the beginning
df = df[['UniqueID'] + [col for col in df.columns if col != 'UniqueID']]

# Display the DataFrame with the new 'UniqueID' column
print(df[:10])

unique_id_count = df['UniqueID'].nunique()
print(f'Count of unique values in UniqueID: {unique_id_count}')


# Specify the file path where you want to save the CSV file
output_file_path = 'pre_processed/cleaned_data.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)