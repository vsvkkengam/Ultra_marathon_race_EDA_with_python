Analyzing a dataset containing records of ultra-marathon races spanning over two centuries. The script performs various data cleaning and exploration tasks using the pandas and seaborn libraries. Below is a description you can use for uploading to a GitHub repository:

---

## Ultra-Marathon Race Analysis

This repository contains a Python script for analyzing a dataset of ultra-marathon race records registered between 1798 and 2022. Ultra-marathon races are footraces longer than the traditional marathon length of 42.195 kilometers (26 miles 385 yards), with various distances ranging from 31 miles (50 kilometers) to over 200 miles (320 kilometers).

### Dataset Description
The dataset comprises 7,461,226 ultra-marathon race records from 1,641,168 unique athletes. The original data, sourced from public websites, has been anonymized to comply with data protection laws, replacing athlete names with unique numerical IDs.

### Script Overview
The Python script performs the following tasks:
- Imports necessary libraries, including pandas and seaborn.
- Loads the dataset from a CSV file.
- Cleans the data by filtering for specific race criteria (e.g., 50 kilometers or 50 miles races in the USA in the year 2020) and handling missing or inconsistent values.
- Performs data exploration and visualization using seaborn, including histograms, violin plots, and gender-specific race performance comparisons.
- Renames columns for better clarity and reorders them as needed.
- Conducts analysis on race lengths and athlete performance.

### Usage
To use the script:
1. Ensure you have Python installed on your system along with the required libraries.
2. Download the dataset provided in CSV format.
3. Update the file path in the script to point to the dataset.
4. Run the script in your preferred Python environment.

### Dependencies
- Python 3.x
- pandas
- seaborn

---
