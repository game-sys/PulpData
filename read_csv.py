import pandas as pd
import matplotlib.pyplot as plt

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

# Create a bar chart with colors and count labels
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# Define custom colors for bars
colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightsteelblue', 'lightyellow', 'lightgray', 'lightblue', 'lightgreen']

# Create bars with labels and count values
bars = plt.bar(tooth_jaw_counts.index, tooth_jaw_counts['Count'], color=colors)
plt.xlabel('Tooth# and Jaw')
plt.ylabel('Count')
plt.title('Count of Tooth# and Jaw Combinations')
plt.xticks(tooth_jaw_counts.index, [f'{tooth} {jaw}' for tooth, jaw in zip(tooth_jaw_counts['Tooth#'], tooth_jaw_counts['Jaw'])], rotation=45, ha='right')

# Add count labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()

# Show the colorful bar chart with count labels
plt.show()





# # Group the DataFrame by 'Tooth#' and 'Jaw'
# grouped = df.groupby(['Tooth#', 'Jaw'])

# # Iterate through each group and save it to a CSV file
# for name, group in grouped:
#     tooth, jaw = name
#     filename = f'tooth{tooth}{jaw}.csv'
#     group.to_csv('Processed/'+filename, index=False)
#     print(f'Saved {filename}')

print('done')