# GitHub Repository Analysis (Python)

Exploratory data analysis of GitHub repository data using Python, Pandas, and Matplotlib.  
This project analyzes repository engagement, programming language trends, and the performance difference between Python loops and vectorized operations.

---

## Features

- **Data preprocessing**
  - Handles missing values
  - Fills missing `Language` values with `"Unknown"`
  - Filters out repositories with zero stars or forks

- **Repository engagement**
  - Computes a **forks-to-stars ratio** as an engagement metric

- **Performance comparison**
  - Benchmarks **Python loops vs Pandas/NumPy vectorization** for computing the engagement ratio

- **Programming language analysis**
  - Identifies the most common programming languages across repositories
  - Calculates **average stars by language** (only languages with ≥500 repositories)

- **AI repository detection**
  - Flags repositories using keyword matching in `Description`
  - Keywords include machine learning, deep learning, artificial intelligence, neural networks, computer vision, and data science

- **Visualization**
  - Generates plots using **Matplotlib**

---

## Dataset

The dataset is included in this repository:

```
data/github_repos.csv
```

The dataset contains **215,000+ GitHub repositories** with metadata used for exploratory analysis.

**Key columns used in the analysis:**

- `Language`
- `Stars`
- `Forks`
- `Description`

---

## How to Run

From the project root:

```bash
pip install -r requirements.txt
python src/github_analysis.py
```

---

## Output

The script will:

- Print dataset summary information and missing value counts
- Compare execution time between Python loops and vectorized operations
- Generate visualizations:
  - Top programming languages by frequency
  - Average stars by language (≥500 repositories)
  - AI vs non-AI repository popularity
  - Stars vs Forks scatter plot (log scale)

---

## Example Findings

- Vectorized Pandas operations were approximately **19× faster** than equivalent Python loops when computing the forks-to-stars engagement ratio.

- The dataset contains repositories written in **368 different programming languages**, with a small number of languages accounting for most repositories.

- AI-related repositories had **higher average star counts** than non-AI repositories in the dataset.

- The relationship between **stars and forks** follows a strong positive trend, which becomes clearer when plotted on a logarithmic scale.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib

---

## Purpose

This project was developed to practice:

- Exploratory data analysis (EDA)
- Data cleaning and preprocessing with Pandas
- Performance comparison between Python loops and vectorized operations
- Visualization of trends in large-scale repository data