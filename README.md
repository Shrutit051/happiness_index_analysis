# Happiness Index Analysis 

## Overview
This project analyzes the **World Happiness Index (2019)** dataset using Python, **pandas**, **matplotlib**, and **seaborn** to perform data analysis and visualization. It explores various statistical measures, relationships between variables, and visualizes data trends.

## Dataset
The dataset consists of **happiness scores and contributing factors** from different countries in 2019. It is stored in CSV format inside the **dataset sheets** directory.
You can get the dataset from here -
```bash
import kagglehub

Download latest version
path = kagglehub.dataset_download("unsdsn/world-happiness")

print("Path to dataset files:", path)
```
Or simply follow this link - 
```bash
https://www.kaggle.com/datasets/unsdsn/world-happiness
```
Google colab link -
```bash
https://colab.research.google.com/drive/11V-3mSFvW379oDPy27MJHcXoWuRxTqWu?usp=sharing
```


## File Structure
```
|-- dataset sheets
|   |-- 2015.csv
|   |-- 2016.csv
|   |-- 2017.csv
|   |-- 2018.csv
|   |-- 2019.csv
|
|-- plots
|   |-- boxplot_score.png
|   |-- histogram1.png
|   |-- histogram2.png
|   |-- histogram3.png
|   |-- line plot.png
|   |-- scatter plot.png
|
|-- README.md
|-- happiness_index_analysis.py
```

## Features
### 1. **Data Analysis**
- Displaying key information about the dataset (shape, column names, data types, etc.)
- Extracting and analyzing specific columns
- Calculating **max, min, mean, mode, median, standard deviation, variance, and skewness** of the Happiness Score

### 2. **Data Visualization**
- **Histogram**: Distribution of Happiness Scores
- **Boxplot**: Spread and outliers in the Happiness Scores
- **Scatter Plot**: Relationship between **Healthy Life Expectancy** and **Freedom to Make Life Choices**
- **Line Plot**: Trends in Happiness Scores across the dataset
- **Correlation Heatmap**: Displays correlations between dataset attributes

## Installation & Requirements
### **Prerequisites**
Ensure you have Python and the required libraries installed.

```bash
pip install pandas matplotlib seaborn
```

### **Running the Analysis**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/happiness-index-analysis.git
   ```
2. Navigate to the project folder:
   ```bash
   cd happiness-index-analysis
   ```
3. Run the analysis script:
   ```bash
   python happiness_index_analysis.py
   ```

## Results
The generated visualizations are saved in the **plots/** directory and provide insights into global happiness trends.

## Future Enhancements
- Expand the dataset to include **multiple years** for trend analysis.
- Implement **machine learning models** to predict happiness scores.
- Add an **interactive dashboard** for better user experience.
- collect data from college students, analyze and draw conclusions about correlation between student lifestyles and happiness index/score
---

Feel free to contribute and improve this project! 🚀

