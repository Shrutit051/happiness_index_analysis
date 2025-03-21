# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:52:18 2025

@author: CCOEW
"""
import pandas as pd
import matplotlib as plt # type: ignore
#import seaborn as sns

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
# Select only numerical features for correlation analysis
numerical_df = df.select_dtypes(include=['number'])

# Calculate correlations for numerical features
plt.figure(figsize=(10, 8))
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Select only numerical features for correlation analysis
numerical_df = df.select_dtypes(include=['number'])

# Calculate correlations for numerical features
plt.figure(figsize=(10, 8))
sns.heatmap(numerical_df.corr(), annot=True, cmap='Spectral')
plt.title('Correlation Heatmap')
plt.show()

import plotly.express as px
# Plotly Choropleth Map
fig = px.choropleth(df, 
                     locations="Country or region", 
                     locationmode="country names",
                     color="Score", 
                     hover_name="Country or region",
                     title="Global Happiness Score (2019)",
                     color_continuous_scale=px.colors.sequential.Plasma)

fig.show()

# Selecting key features
selected_features = ["Score", "GDP per capita", "Healthy life expectancy", "Social support"]

# Pairplot
sns.pairplot(df[selected_features], diag_kind="kde")
plt.show()

plt.figure(figsize=(8, 6))
sns.kdeplot(df["Score"], shade=True, color="blue", label="Happiness Score")
sns.kdeplot(df["GDP per capita"], shade=True, color="green", label="GDP per Capita")
sns.kdeplot(df["Healthy life expectancy"], shade=True, color="red", label="Life Expectancy")
plt.legend()
plt.title("KDE Plot of Key Variables")
plt.show()

#linear regression
# Selecting features (X) and target (y)
X = df[['GDP per capita', 'Healthy life expectancy', 'Social support']]
y = df['Score']

# Check for missing values
#print("Missing values before filling:", df.isnull().sum())

# Fill numeric columns with the mean (Fixes FutureWarning)
for column in df.select_dtypes(include=['number']).columns:
    df.loc[:, column] = df[column].fillna(df[column].mean())

# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)

# Evaluate the model
print("Linear Regression Performance:")
print("MSE:", mean_squared_error(y_test, y_pred_lr))
print("R² Score:", r2_score(y_test, y_pred_lr))


plt.scatter(y_test, y_pred_lr, label="Linear Regression", alpha=0.6)
#plt.scatter(y_test, y_pred_rf, label="Random Forest", alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="--")
plt.xlabel("Actual Happiness Score")
plt.ylabel("Predicted Happiness Score")
plt.title("Regression Model Predictions")
plt.legend()
plt.show()

#random forest predictions
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

# Evaluate Random Forest
print("Random Forest Performance:")
print("MSE:", mean_squared_error(y_test, y_pred_rf))
print("R² Score:", r2_score(y_test, y_pred_rf))

plt.scatter(y_test, y_pred_rf, label="Random Forest", alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="--")
plt.xlabel("Actual Happiness Score")
plt.ylabel("Predicted Happiness Score")
plt.title("Regression Model Predictions")
plt.legend()
plt.show()









