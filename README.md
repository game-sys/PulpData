# PulpData: Dental Pulp Data PreProcessing

Welcome to the PulpData repository! This project focuses on preprocessing and analyzing dental pulp data, with the aim of extracting valuable insights from the dataset.

## Overview

Dental pulp data often contains critical information related to patients' oral health. This repository provides a set of data preprocessing and analysis techniques to harness this information effectively. The project includes the following key components:

### 1. Summary Statistics

![Summary Statistics](images/summary_statistics.png)

We start by calculating and visualizing essential summary statistics for the dataset. This includes measures like mean, median, standard deviation, minimum, and maximum for relevant numeric columns. These statistics give us an initial understanding of the central tendencies and spreads in the data.

### 2. Tooth Count Analysis

![Tooth Count](images/tooth_count.png)

Understanding tooth counts can be vital in dental research. We analyze and visualize tooth count data to gain insights into the distribution and frequency of different tooth numbers within the dataset.

### 3. Correlation Analysis

<img src="images/correlation_matrix.png" alt="Correlation Matrix" width="800" height="700">

Correlation analysis helps identify relationships between variables. We calculate the correlation matrix between numeric features, including "CEJ to Pulp horn (mm)," "CEJ to cusp tip (mm)," and "Tooth-coronal index," and target variables like "Age" and "Gender." This analysis helps us identify which features are most strongly associated with the targets.

<!--- Furthermore, analysis for each file was conducted for deep analysis.

#### Correlation Matrix for tooth3Mandible.csv:
<img src="images/correlation_matrix_tooth3Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth3Maxilla.csv:
<img src="images/correlation_matrix_tooth3Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth4Mandible.csv:
<img src="images/correlation_matrix_tooth4Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth4Maxilla.csv:
<img src="images/correlation_matrix_tooth4Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth5Mandible.csv:
<img src="images/correlation_matrix_tooth5Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth5Maxilla.csv:
<img src="images/correlation_matrix_tooth5Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth6Mandible.csv:
<img src="images/correlation_matrix_tooth6Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth6Maxilla.csv:
<img src="images/correlation_matrix_tooth6Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth7Mandible.csv:
<img src="images/correlation_matrix_tooth7Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth7Maxilla.csv:
<img src="images/correlation_matrix_tooth7Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth8Mandible.csv:
<img src="images/correlation_matrix_tooth8Mandible.csv.png" alt="Correlation Matrix" width="800" height="700">

#### Correlation Matrix for tooth8Maxilla.csv:
<img src="images/correlation_matrix_tooth8Maxilla.csv.png" alt="Correlation Matrix" width="800" height="700"> --->

### 4. Scatterplots

![Scatterplots - Age](images/scatterplots_age.png)

![Scatterplots - Gender](images/scatterplots_gender.png)

Scatterplots provide a visual way to assess relationships between numeric features and target variables. We create scatterplots to visualize these relationships, enabling us to detect trends, patterns, and potential outliers in the data. Scatterplots are generated for "CEJ to Pulp horn (mm)," "CEJ to cusp tip (mm)," and "Tooth-coronal index" against both "Age" and "Gender."

# Project Results

## Gender Classification (Ensemble Model):

- Random Forest Accuracy 1 (tooth5): 0.6589595375722543
- Random Forest Accuracy 2 (tooth6): 0.6589595375722543
- Random Forest Accuracy 3 (tooth7): 0.6242774566473989
- Random Forest Ensemble Accuracy final: 0.6936416184971098

## Age-group Classification (Ensemble Model):

- Random Forest Accuracy 1 (tooth5): 0.6069364161849711
- Random Forest Accuracy 2 (tooth6): 0.6011560693641619
- Random Forest Accuracy 3 (tooth7): 0.49710982658959535
- Random Forest Ensemble Accuracy final: 0.7052023121387283



## Getting Started

To replicate the analysis or explore the dental pulp data preprocessing techniques, follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have the necessary Python libraries installed, such as pandas, matplotlib, seaborn, and Pillow (PIL).

3. Access the Jupyter Notebook or Python scripts within the repository to execute the data preprocessing and analysis steps.

4. Customize the code and visuals as needed for your specific dental pulp dataset.

## Contribute

We welcome contributions from the community! If you have ideas for improvements, additional analysis techniques, or visualizations, feel free to create a pull request or open an issue. Together, we can enhance our understanding of dental pulp data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Thank you for your interest in the PulpData project. We hope it proves valuable for your dental research and data preprocessing needs.
