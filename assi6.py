# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:52:18 2025

@author: CCOEW
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/CCOEW/Desktop/469 dataset/2019.csv')

# Display the full DataFrame
print(df.head())
print(df.shape)
print(df.tail)
print(df.columns)
print(df.info)
print(df.loc[10])
print(df.iloc[-1])

subset_df = df[['Overall rank', 'Country or region', 'Score']]
print(subset_df.head())

# data analysis
max_value = df['Score'].max()
print(f"Country ... has a maximum score of: {max_value}")

min_value = df['Score'].min()
print(f"Country ... has a minimum score of: {min_value}")

# Find mean
mean_value = df['Score'].mean()
print(f"Mean value in Score: {mean_value}")

# Find mode
mode_value = df['Score'].mode()[0]
print(f"Mode value in Score: {mode_value}")

# Find median
median_value = df['Score'].median()
print(f"Median value in Score: {median_value}")

# Find standard deviation
std_dev = df['Score'].std()
print(f"Standard deviation in Score: {std_dev}")

# Find variance
variance = df['Score'].var()
print(f"Variance in Score: {variance}")

# Find skewness
skewness = df['Score'].skew()
print(f"Skewness in Score: {skewness}")

#data visualization
#histogram
plt.hist(df['Score'], bins=50, edgecolor='black')
plt.hist(df['Score'], bins=75, edgecolor='white')
plt.title('Histogram of scores')
plt.xlabel('Score')
plt.ylabel('Number of countries')
plt.show()

#boxplot
plt.boxplot(df['Score'])
plt.title('Boxplot of Score column')
plt.ylabel('Score')
plt.show()

#scatter plot
plt.scatter(df['Healthy life expectancy'], df['Freedom to make life choices'], color='blue')
plt.title('Scatter plot of Health life expentancy VS Freedom to make life choices')
plt.xlabel('col1')
plt.ylabel('cool2')
plt.show()

#line plot
plt.plot(df['Score'], color='red')
plt.title('Line plot of Happiness Score')
plt.xlabel('Index')
plt.ylabel('Happiness Score')
plt.show()

#correlation heatmap

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation heatmap')
plt.show()







