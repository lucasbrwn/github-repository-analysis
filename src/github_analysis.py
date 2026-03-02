"""
GitHub Repository Analysis

This script performs exploratory data analysis (EDA) on GitHub repository data,
including:
- Data cleaning and preprocessing
- Loop vs. vectorization performance comparison
- Language frequency analysis
- Average stars by language
- AI-related repository analysis using keyword matching
- Stars vs. Forks visualization (log scale)
"""

import time
import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "data/github_repos_sample.csv" # sample of dataset (recommended for GitHub)
# FULL_PATH = "data/github_repos.csv"      # local dataset (not committed)

df = pd.read_csv(DATA_PATH)

print("First 5 rows")
print(df.head())

print("Last 5 rows")
print(df.tail())

print("Shape: ")
print(df.shape)

print("Statistical Summary: ")
print(df.describe())

sum_nulls = df.isna().sum()
print(sum_nulls)

replacement = 'Unknown'
df['Language'] = df['Language'].fillna(replacement)
print(df['Language'].isna().sum())

replacement2 = ((df['Stars'] > 0) & (df['Forks'] > 0))
df = df[replacement2]
print("Filtered shape:", df.shape)

# Python Loop vs Vectorization Benchmark

py_ratio = []

stars = df["Stars"].to_list()
forks = df["Forks"].to_list()

start = time.time()

for s, f in zip(stars, forks):
  py_ratio.append(f / s)

python_time = time.time() - start
print(f"Python Loop took: {python_time:.6f} seconds")

start=time.time()
df['viral_ratio'] = df['Forks']/df['Stars']

np_pd_time = time.time() - start
print(f"NumPy/Pandas Vectorization took: {np_pd_time:.6f} seconds")

print(f"Speedup (loop / vectorized): {python_time / np_pd_time:.2f}x")

# Vectorization is faster because pandas/NumPy run operations at once rather than looping row by row

# Language Frequency Plot

lang_df = df[df['Language'] != 'Unknown']

frequency = lang_df.groupby('Language').size().sort_values(ascending=False)

top_10_frequency = frequency.head(10)

data = {
    'Language' : top_10_frequency.index,
    'Frequency' : top_10_frequency.values
}

freq_df = pd.DataFrame(data)

plt.bar(freq_df['Language'], freq_df['Frequency'])
plt.xlabel('Language')
plt.ylabel('Frequency')
plt.title('Top 10 Programming Languages')
plt.xticks(rotation=45, ha='right')
plt.show()

# Average Stars by Language (only Languages with >= 500 repos)

mean_star_count = lang_df.groupby('Language')['Stars'].mean().sort_values(ascending=False)
print(mean_star_count)

above_500 = frequency >= 500

repo_above_500 = mean_star_count[above_500]
repo_above_500 = repo_above_500.sort_values(ascending=False)

top_10_above_500 = repo_above_500.head(10)

data1 = {
    'Language' : top_10_above_500.index,
    'Average Stars' : top_10_above_500.values
}

freq_df1 = pd.DataFrame(data1)

plt.bar(freq_df1['Language'], freq_df1['Average Stars'])
plt.xlabel('Language')
plt.ylabel('Average Stars')
plt.title('Top 10 Programming Languages by Average Stars with More than 500 Repositories')
plt.xticks(rotation=45, ha='right')
plt.show()

# AI Keyword Flag + Average Stars

myKeywords = ['machine learning', 'deep learning', 'artificial intelligence', 'neural network', 'computer vision', 'data science']
pattern = '|'.join(myKeywords)
df['is_ai'] = df['Description'].str.contains(pattern, case=False, na=False)

avg_ai = df.groupby('is_ai')['Stars'].mean()
print(avg_ai)

# Stars vs Forks Scatter Plot (log scale)

plt.figure(figsize=(10, 6))
star_filter = df['Stars'] < 50000
df_scatter = df[star_filter]
plt.scatter(df_scatter['Stars'], df_scatter['Forks'], alpha=0.5)
plt.xlabel('Stars')
plt.ylabel('Forks')
plt.title('Stars vs Forks')
plt.grid(True, linestyle='--', alpha=0.2)
plt.xscale('log')
plt.yscale('log')
plt.show()