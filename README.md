GitHub Repository Analysis

Exploratory data analysis of GitHub repository data using Python, Pandas, and Matplotlib.
This project analyzes repository engagement, programming language trends, and the performance difference between Python loops and vectorized operations.

Overview

This project performs exploratory data analysis (EDA) on a dataset of GitHub repositories. The analysis includes:

Data cleaning and preprocessing

Handling missing values

Filtering invalid records

Computing a forks-to-stars engagement metric

Comparing Python loops vs Pandas/NumPy vectorization

Analyzing programming language popularity

Identifying AI-related repositories

Visualizing trends using Matplotlib

Dataset

This project expects a CSV file located at:

data/github_repos.csv

The dataset is not included in this repository.

Required columns

Language

Stars

Forks

Description

How to Run
1. Install dependencies
pip install -r requirements.txt
2. Place the dataset

Put your CSV file in:

data/github_repos.csv
3. Run the analysis
python src/github_analysis.py
Output

The script will:

Print dataset summary information

Compare execution time between Python loops and vectorized operations

Generate visualizations:

Top programming languages by frequency

Average stars by language

AI vs non-AI popularity

Stars vs Forks scatter plot (log scale)

Tech Stack

Python

Pandas

NumPy

Matplotlib