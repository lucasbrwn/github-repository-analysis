"""
My use of AI in this project was to help me understand both Pandas and Matplotlib functionality. Specifically, I asked AI to explain certain methods like .index and .values and to clarify functions used in my professor's Jupyter notebook so that I could determine how to implment them in my project.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/github_repos.csv"
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
print(df['Stars'], df['Forks'])

import time

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
print(f"Numpy/Pandas Vectorization took: {np_pd_time:.6f} seconds")

print(f"Speedup (loop / vectorized): {python_time / np_pd_time:.2f}x")

"""Vectorization is faster because it does all of the required math at once rather than in a loop that Python uses. A Python list in this case has to loop over each row one by one then calculate the ratio rather than being able to do all calculations at once using vectorization."""

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

myList = ['machine learning', 'deep learning', 'artificial intelligence', 'neural network', 'computer vision', 'data science']
pattern = '|'.join(myList)
df['is_ai'] = df['Description'].str.contains(pattern, case=False, na=False)

avg_ai = df.groupby('is_ai')['Stars'].mean()
print(avg_ai)

"""The AI hype is real and proven in this data set. By average stars, AI is given around 500 more stars than a repository with no AI usage. This suggests that the use of AI in a repository will increase Stars."""

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