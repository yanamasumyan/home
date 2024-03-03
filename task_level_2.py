# 1. Installing Python and Pandas
#    ● Task: Install Python and the Pandas library
#      on your computer.Verify the installation by 
#      running a simple script to print the Pandas version.

#  pip install pandas

import pandas as pd
print("Version of Pandas")
print(pd.__version__)


# 2. Exploring Pandas Data Structures
#    ● Task: Create a Pandas DataFrame manually by defining
#      a dictionary of lists, where each key-value pair represents
#      a column and its values. Practice accessing and manipulating
#      individual columns and rows.

import pandas as pd

# Creating a dictionary containing student information
students = {
    'Name': ['Jane', 'Andrew', 'Angel', 'Suzie'],
    'Age': [27, 34, 21, 31],
    'Profession': ['Data Scientist', 'Software Developer','Graphic Designer','Project Manager']

}

# Creating a DataFrame from the dictionary
st = pd.DataFrame(students)

# Printing the DataFrame
print("\nDataFrame:")
print(st)

# Printing the column 'Name'
print("\nColumn Name:")
print(st['Name'])

# Printing the column 'Age'
print("\nColumn Age:")
print(st.Age)

# Printing the column 'Profession'
print("\nColumn Profession:")
print(st.Profession)

# Accessing and printing the second row of the DataFrame
print("\nAccessing the second row:")
print(st.iloc[1])
print()


# 3. Loading Data into a DataFrame
#    ● Task: Load a simple CSV file into a Pandas DataFrame.
#      Use basic commands to explore the first few rows, data
#      types of each column, and summary statistics.

import pandas as pd

path = r'C:\Users\User\Desktop\CSV\data.csv'

# Reading the CSV file into a DataFrame
df = pd.read_csv(path)
# df = pd.read_csv(path, nrows=3)

print("Reading CSV file:")
# Printing the DataFrame
print(df)

# Extracting and printing a few rows of the DataFrame
few_rows = df.head(3) 
print("\nFew rows:")  
print(few_rows)

# Printing data types of columns in the DataFrame
print("\nData types:") 
print(df.dtypes)

# Printing summary statistics of the DataFrame
print("\nSummary statistics:") 
print(df.describe())


# 4. Basic Data Selection and Filtering
#    ● Task: Given a DataFrame, practice selecting columns using their
#      names and filtering rows based on specific criteria 
#      (e.g., select rows where a column’s value is greater than a threshold).

import pandas as pd

students = {
    'Name': ['Jane', 'Andrew', 'Angel', 'Suzie'],
    'Age': [27, 24, 21, 31],
    'Profession': ['Data Scientist', 'Software Developer','Graphic Designer','Project Manager']

}

# Creating a DataFrame 
st = pd.DataFrame(students)

# Printing the DataFrame
print("\nDataFrame:")
print(st)

# Selecting the first Name from the DataFrame
print("\nSelect first Name:")
print(st['Name'][0])

# Selecting specific columns from the DataFrame
print("\nSelected columns:")
print(st[['Name','Profession']])

# Filtering rows based on a condition
print("\nFiltering rows:")
print(st[st['Age'] > 25])


# 5. Introduction to Handling Missing Data
#    ● Task: Identify missing values in a DataFrame. 
#      Practice using the isna() function to find missing values
#      and the dropna() function to remove rows with missing values

import pandas as pd

students = {
    'Name': ['Jane', None, 'Angel', 'Suzie'],
    'Age': [27, 24, 21, 31],
    'Profession': ['Data Scientist', 'Software Developer',None,'Project Manager']
}

# Creating a DataFrame
st = pd.DataFrame(students)

# Printing missing values in the DataFrames
print("\nMissing values:")
print(st.isna())


# 6. Basic Data Visualization
#    ● Task: Use Pandas' built-in plotting capabilities
#      to create simple visualizations like histograms or
#      bar charts for selected columns in the DataFrame.

import pandas as pd
import matplotlib.pyplot as plt

employees = {
    'Name': ['Jane', 'Bob', 'Angel', 'Charlie','Suzie'],
    'Age': [27, 31, 22, 43, 37],
    'Salary': [200000,350000,150000,500000,420000]
}

# Creating a DataFrame
df = pd.DataFrame(employees)

# df.plot.area
df.plot.area(x='Name', y='Salary')
plt.title('Area Plot')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# df.plot.barh
df.plot.barh(x='Name', y='Age')
plt.title('Barh Plot')
plt.xlabel('Age')
plt.ylabel('Name')
plt.show()

# df.plot.density
df['Salary'].plot.density(color='green', bw_method=0.3)
plt.title('Denisty Plot')
plt.xlabel('Salary')
plt.show()

# df.plot.hist
df['Age'].plot.hist(bins=7, color = 'skyblue')
plt.title('Hist Plot')
plt.xlabel('Age')
plt.ylabel('Frequency') 
plt.show()

# df.plot.line
df.plot.line(x='Name',y='Salary')
plt.title('Line Plot')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# df.plot.scatter
df.plot.scatter(x='Name', y='Salary', c = 'red')
plt.title('Scatter Plot')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# df.plot.bar
df.plot.bar(x='Name', y='Salary', rot = 0)
plt.title('Bar Plot')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# df.plot.box
df.plot.box(y='Salary')
plt.title('Box Plot')
plt.ylabel('Salary')
plt.show()

# df.plot.hexbin
df.plot.hexbin(x='Age', y='Salary', gridsize=10)
plt.title('Hexbin Plot')
plt.show()

# df.plot.kde
df['Salary'].plot.kde()
plt.title('Kde Plot')
plt.xlabel('Salary')
plt.show()

# df.plot.pie
df.plot.pie(y='Salary', autopct='%1.0f%%')
plt.title('Pie Plot')
plt.ylabel('Salary')
plt.show()


# 7. Manipulating DataFrame Columns
#    ● Task: Add a new column to a DataFrame, calculated from existing columns
#      (e.g., a total or average). Practice renaming and deleting columns.

import pandas as pd
import matplotlib.pyplot as plt

employees = {
    'Name': ['Jane', 'Bob', 'Angel', 'Charlie','Suzie'],
    'Salary': [200000,350000,150000,500000,420000]
}

# Creating a DataFrame
df = pd.DataFrame(employees)
print()

# Adding 'Age' column to the DataFrame
df.insert(1,'Age',[27, 31, 22, 43, 37], True)

# Adding 'Coefficient' column to the DataFrame
df.insert(3,'Coefficient',[2,1.5,2,3,1.2])

# Calculating 'Salary_Increase' based on 'Salary' and 'Coefficient'
df['Salary_Increase'] = df['Salary'] * df['Coefficient']

# Adding 'Total' column which includes original salary and salary increase
df['Total'] = df['Salary'] + df['Salary_Increase']

# Printing the DataFrame
print(df)
print()

# Renaming columns 'Name' and 'Age' to 'Employee_Name' and 'Employee_Age'
df.rename(columns={'Name':'Employee_Name','Age':'Employee_Age'},inplace=True)
print(df)
print()

# Deleting the 'Salary_Increase' column
del df['Salary_Increase']
print(df)


# 8. Grouping and Aggregating Data
#    ● Task: Group the data by one or more columns and calculate
#      aggregate statistics (e.g., mean, sum) for each group.

import pandas as pd

data = {
    'Gender':['m','f','f','m','f','m','m'],
    'Height':[172,171,169,173,170,175,178]
    }

# Creating a DataFrame
df = pd.DataFrame(data)

# sum(): Compute sum of column values
sum_values = df.groupby('Gender').sum()
print("Sum of values by category:")
print(sum_values)
print()

# min(): Compute min of column values
min_values = df.groupby('Gender').min()
print("Minimum values by category:")
print(min_values)
print()

# max(): Compute max of column values
max_values = df.groupby('Gender').max()
print("Maximum values by category:")
print(max_values)
print()

# mean(): Compute mean of column values
mean_values = df.groupby('Gender').mean()
print("Mean values by category:")
print(mean_values)
print()

# size(): Compute column sizes
size_values = df.groupby('Gender').size()
print("Sizes of groups:")
print(size_values)
print()

# describe(): Generates descriptive statistics
describe_values = df.groupby('Gender').describe()
print("Descriptive statistics:")
print(describe_values)
print()

# first(): Compute first of group values
first_values = df.groupby('Gender').first()
print("First values of each group:")
print(first_values)
print()

# last(): Compute last of group values
last_values = df.groupby('Gender').last()
print("Last values of each group:")
print(last_values)
print()

# count(): Compute count of column values
count_values = df.groupby('Gender').count()
print("Count of values by category:")
print(count_values)
print()

# std(): Standard deviation of column
std_values = df.groupby('Gender').std()
print("Standard deviation by category:")
print(std_values)
print()

# var(): Compute variance of column
var_values = df.groupby('Gender').var()
print("Variance by category:")
print(var_values)
print()

# sem(): Standard error of the mean of column
sem_values = df.groupby('Gender').sem()
print("Standard error of the mean by category:")
print(sem_values)
print()


# 9. Basic String Operations
#    ● Task: Perform basic string operations on a DataFrame column,
#      such as converting to lowercase, stripping whitespace,
#      or splitting strings into lists.

import pandas as pd

data = {
    'Name': ['   John', 'bODAY   ', '  MinA  ', 'Peter', '   nicky  '],
    'Degree': ['masters  ', ' graduate', 'graduate ', 'Masters', 'Graduate   '],
    'Age': [27, 23, 21, 23, 24]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# converting to lowercase
df['Name'] = df['Name'].str.lower()

# stripping whitespace
df['Degree'] = df['Degree'].str.strip()

# splitting strings into lists
df['Name'] = df['Name'].str.split()

print(df)


# 10. Introduction to Data Cleaning Techniques
#     ● Task: Combine the skills learned in previous tasks 
#       to clean a simple dataset. Identify and fill missing 
#       values using the fillna() method with a specified value 
#      (e.g., the mean of the column).

import pandas as pd

path = r'C:\Users\User\Desktop\CSV\table.csv'

# Reading the CSV file into a DataFrame
df = pd.read_csv(path)

# Printing the DataFrame
print(df)

# Converting names to uppercase
df['Name'] = df['Name'].str.upper()

# Splitting names into a list of strings
df['Name'] = df['Name'].str.split()
#df['Name'] = df['Name'].str.strip()

#df.fillna(0.0, inplace=True)

# Filling missing values with mean of respective columns (excluding 'Name' column)
df.fillna(df.drop(columns='Name').mean(), inplace=True)

#df.fillna(df.drop(columns='Name').median(), inplace=True)

# Printing the updated DataFrames
print(df)


# 11. Data Cleaning with Pandas
#     ● Task: Return to the original task with enhanced skills and confidence.
#       Load a dataset, identify missing values, and make decisions on handling 
#       these values through removal or imputation

import pandas as pd

path = r'C:\Users\User\Desktop\CSV\data1.csv'

# Reading the CSV file
df = pd.read_csv(path)

# Printing the original dataset
print('\nOriginal dataset:')
print(df)

# Checking for missing values
print('\nMissing values:')
print(df.isna())

# Filling missing values in 'Height' and 'Weight' columns with mean values
df.fillna({'Height': df['Height'].mean()}, inplace=True)
df.fillna({'Weight': df['Weight'].mean()}, inplace=True)

# Assigning missing value of 'Gender' for 'David' to 'M'
df.loc[df['Name'] == 'David', 'Gender'] = 'M'

# Deleting rows with more than 1 missing values
df = df.drop([2,4], axis=0).reset_index(drop=True)

# Displaying the cleaned dataset
print("\nCleaned dataset:")
print(df)
