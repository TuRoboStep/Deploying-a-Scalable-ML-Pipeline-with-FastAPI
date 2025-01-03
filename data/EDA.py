import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("data/census.csv")

# Display the first few rows of the dataset
print(data.head())

# Display basic information about the dataset
print(data.info())

# Display summary statistics of the dataset
print(data.describe(include='all'))

# Check for missing values
print(data.isnull().sum())

# Plotting the distribution of the 'age' column
plt.figure(figsize=(10, 6))
sns.histplot(data['age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# Plotting the distribution of the 'education' column
plt.figure(figsize=(12, 6))
sns.countplot(y='education', data=data, order=data['education'].value_counts().index)
plt.title('Education Distribution')
plt.show()

# Plotting the relationship between 'age' and 'salary'
plt.figure(figsize=(10, 6))
sns.boxplot(x='salary', y='age', data=data)
plt.title('Age vs. Salary')
plt.show()

# Plotting the relationship between 'education' and 'salary'
plt.figure(figsize=(12, 6))
sns.countplot(y='education', hue='salary', data=data, order=data['education'].value_counts().index)
plt.title('Education vs. Salary')
plt.show()

# Plotting the relationship between 'hours-per-week' and 'salary'
plt.figure(figsize=(10, 6))
sns.boxplot(x='salary', y='hours-per-week', data=data)
plt.title('Hours Per Week vs. Salary')
plt.show()
