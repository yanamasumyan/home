# 1. Advanced Python Data Structures
#   ● Task: Create complex data structures combining lists, 
#     dictionaries, and sets, mimicking a real dataset's 
#     structure. Practice accessing and modifying nested data.

# Define the dataset
movies = [
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "director": "Frank Darabont",
        "genres": {"drama"},
        "cast": [
            {
                "name": "Tim Robbins",
                "role": "Andy Dufresne"
            },
            {
                "name": "Morgan Freeman",
                "role": "Ellis Boyd 'Red' Redding"
            }
        ]
    },

    {
        "title": "The Godfather",
        "year": 1972,
        "director": "Francis Ford Coppola",
        "genres": {"crime", "drama"},
        "cast": [
            {
                "name": "Marlon Brando",
                "role": "Don Vito Corleone"
            },
            {
                "name": "Al Pacino",
                "role": "Don Michael Corleone"
            }
        ]
    },

    {
        "title": "The Green Mile",
        "year": 1999,
        "director": "Frank Darabont",
        "genres": {"crime", "drama", "fantasy"},
        "cast": [
            {
                "name": "Tom Hanks",
                "role": "Paul Edgecomb"
            },
            {
                "name": "David Morse",
                "role": "Brutus 'Brutal' Howell"
            }
        ]
    }
]

# Accessing Data

# Print the title of the second movie.
print("The title of the second movie: ", movies[1]["title"])

# Print the name of the director of the third movie.
print("The name of the director of the third movie: ", movies[2]["director"])

# Print the role of the second cast member of the first movie.
print("The role of the second cast member of the first movie: ",  movies[0]["cast"][1]["role"] )

# Print the genres of the third movie.
print("The genres of the third movie: ", movies[2]["genres"])


# Modifying Data

# Change the year of the second movie to 1974.
movies[1]["year"] = 1972
print(f"The year of the second movie changed to", movies[1]["year"])

# Add a new cast member to the third movie: {"name": "Michael Clarke Duncan", "role": "John Coffey"}.
new_cast = {"name": "Michael Clarke Duncan", "role": "John Coffey"}
movies[2]["cast"].append(new_cast)
print("Updated cast members: ", movies[2]["cast"])

# Add a new genre, "mystery", to the second movie.
new_genre = "mystery"
movies[1]["genres"].add(new_genre)
print("Updated genres: ", movies[1]["genres"])

# Change the role of the first cast member of the third movie to "John Coffey".
movies[2]["cast"][0]["role"] = "John Coffey"
print("Updated roles: ", movies[2]["cast"])


# Additional Challenges

# Write a function to find all movies directed by a given director.
def find_movie_by_director(movies, director_name):
    return [movie for movie in movies if movie["director"] == director_name]

print("\nMovies directed by a given director: ")
print(find_movie_by_director(movies, "Frank Darabont"))

# Write a function to find all movies released after a given year.
def find_movie_by_year(movies, year):
    return [movie for movie in movies if movie["year"] > year]
print("\nAll movies released after a given year: ")
print(find_movie_by_year(movies, 1990))


# 2. Lambda Functions and Map/Reduce
#    ● Task: Use lambda functions along with map() and 
#      reduce() to perform operations on a list of numbers 
#      (e.g., converting temperatures, aggregating data).

from functools import reduce

# Converting Celsius temperatures to Fahrenheit with lambda function and map()
c_temperatures = [24, 35, 9, 48, 17]
f_temperatures = list(map(lambda c: c*9/5+32, c_temperatures))
print("\nCelsius temperatures: ",c_temperatures)
print("Fahrenheit temperatures: ",f_temperatures)

# Squaring numbers using lambda function and map()
numbers = [3,4,6,7,8]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Aggregating data with lambda function and reduce()
numbers = [2,6,3,9,7,1,8]
sum_of_numbers = reduce(lambda x,y: x+y, numbers)
print("Sum of numbers: ",sum_of_numbers)

# Joining words into a sentence with lambda function and reduce()
words = ["Aggregating", "data", "with", "lambda", "function"]
sentence = reduce(lambda x,y: x + ' ' + y, words)
print(sentence)

# Finding the maximum number in a list with lambda function and reduce()
ls = [7,2,8,5,1,9]
result = reduce(lambda x,y: x if x > y else y, ls)
print(result)


# 3. Pandas Dataframe Manipulations
#    ● Task: Given a sample DataFrame, practice adding 
#      and removing columns, filtering rows based on 
#      conditions, and merging two DataFrames on a key.

import pandas as pd

# Define the datasets
data1 = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500],
    'D': [1000,2000,3000,4000,5000],
}

data2 = {
    'C': [300,100,500],
    'D': [4000,2000,3000]
}

# First DataFrame
df1 = pd.DataFrame(data1)
print("Original DataFrame data1")
print(df1)

# Second DataFrame
df2 = pd.DataFrame(data2)
print("\nOriginal DataFrame data2")
print(df2)

# Adding a new column
print("\nDataFrame after adding")
df1['E'] = [10000,20000,30000,40000,50000]
print(df1)

# Removing a column
print("\nDataframe after removing")
df1 = df1.drop(['D','E'], axis=1)
print(df1)

# Filtering rows based on conditions
print("\nFiltered DataFrame")
filtered_df = df1[df1['B'] > 20]
print(filtered_df)

# Merging two DataFrames on a key
print("\nMerged DataFrame")
merged_data = pd.merge(df1, df2, on='C')
print(merged_data)


# 4. Handling Date and Time Data
#    ● Task: Work with a dataset containing date and time columns.
#      Convert string dates to datetime objects, extract components
#      like day and month, and perform time-based filtering.

import pandas as pd

# Define the dataset
data = {
    'date': ['2019-01-07', '2007-02-11', '2023-03-25', '2014-04-30'],
    'time': ['23:15', '08:30', '11:11', '17:40']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Convert 'date' and 'time' columns to datetime objects
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'])

# Extract components from 'date' column
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month

# Extract components from 'time' column
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute

# df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# Display filtered DataFrame
print("\nFiltered DataFrame:")
# Filter DataFrame based on time 
df_filtered = df[(df['time'] >= '10:00') & (df['time'] <= '18:00')]

# Filter DataFrame based on date 
#df_filtered = df[df['date'] > '2017-01-01']
print(df_filtered)


# 5. Data Cleaning with Pandas
#    ● Task: Load a dataset (e.g., the Titanic dataset available on Kaggle) using Pandas.
#      Identify and handle missing values in the dataset by either removing rows/columns with
#      missing values or imputing them with median or mode values.

import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Loading the dataset
path = 'titanic.csv'
df = pd.read_csv(path)

# Identify missing values
missing_data = df.isna()
missing_data.to_csv('missing_data.csv', index=False)

# Visualisation with Bar chart
msno.bar(df)
plt.title('Percentage of Missing Values')
plt.show()

# Removing column 'Cabin'
df.drop(columns=['Cabin'], inplace=True)

# Filling missing values in 'Age' column with mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Filling missing values in 'Embarked' column with the most common value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Saving the modified dataset to a new CSV file
df.to_csv('new_titanic.csv', index=False)


# 6. Complex Data Aggregations
#    ● Task: Use GroupBy functionality in Pandas to aggregate data from a DataFrame,
#      calculating grouped statistics (e.g., average sales per month).

import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

path = 'statsfinal.csv'
df = pd.read_csv(path)

# Identify missing values
mis_data = df.isna().sum()
print(mis_data)
#mis_data.to_csv('mis_data.csv', index=False)

# Visualisation with Bar chart
msno.bar(df)
plt.title('Percentage of Missing Values')
plt.show()

# Unique values 
unique_dates = df['Date'].unique()
print(unique_dates)

# Parse dates manually
for date in unique_dates:
    try:
        pd.to_datetime(date, format='%d-%m-%Y')
    except ValueError:
         print("Unable to parse date:", date)

# Convert to datetime type and find data with NaTs
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Remove rows with NaTs
df = df.dropna(subset=['Date'])

# Compute average sales per month for each year
average_sales = df.groupby(['Year', 'Month'])[['Q-P1', 'Q-P2', 'Q-P3', 'Q-P4']].mean()

# Round average sales to two decimal places
average_sales = average_sales.round(2)
print("Average sales per month for each year:\n", average_sales)

# Save the results to a CSV file
average_sales.to_csv('average_sales.csv')  

# Plot a line graph for average sales
average_sales.plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.title('Average Sales per Month per Year')
plt.legend(title='Product')
plt.grid(True)
plt.show()













