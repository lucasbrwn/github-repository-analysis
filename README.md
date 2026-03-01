\# GitHub Repository Analysis



Exploratory data analysis of GitHub repository data using Python, Pandas, and Matplotlib.  

This project analyzes repository engagement, programming language trends, and the impact of AI-related topics while also comparing Python loop performance to Pandas/NumPy vectorization.



---



\## Overview



This project performs exploratory data analysis (EDA) on a dataset of GitHub repositories. The analysis focuses on:



\- Data cleaning and preprocessing

\- Handling missing values

\- Filtering invalid records

\- Creating a forks-to-stars engagement metric

\- Comparing Python loops vs vectorized operations

\- Identifying trends in programming language usage

\- Measuring the popularity of AI-related repositories

\- Visualizing results using Matplotlib



---



\## Key Features



\### Data Processing

\- Loaded and inspected dataset structure and summary statistics

\- Handled missing values in the `Language` column

\- Filtered repositories with invalid star/fork counts



\### Performance Comparison

\- Implemented a Python loop to compute a forks-to-stars ratio

\- Implemented a Pandas/NumPy vectorized version

\- Measured execution time for both approaches

\- Demonstrated the efficiency of vectorized operations



\### Exploratory Analysis

\- Top programming languages by repository frequency

\- Top languages by average stars (with sufficient sample size)

\- Detection of AI-related repositories using keyword matching

\- Comparison of average stars for AI vs non-AI projects



\### Visualization

\- Bar charts for language frequency and popularity

\- Log–log scatter plot of Stars vs Forks

\- Visual analysis of repository engagement patterns



---



\## Dataset



This project expects a CSV file located at:

data/github\_repos.csv





The dataset is not included in this repository.



Required columns include:

\- `Language`

\- `Stars`

\- `Forks`

\- `Description`



---



\## How to Run



\### 1. Install dependencies



pip install -r requirements.txt



\### 2. Place the dataset



Put your CSV file in the following location:



data/github\_repos.csv



\### 3. Run the analysis



python src/github\_analysis.py

