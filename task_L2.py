# 1. Installing Python and Pandas
#  pip install pandas

import pandas as pd

print(pd.__version__)


# 2. Exploring Pandas Data Structures
import pandas as pd

student = {
    'Name': ['Jane', 'Andrew', 'Angel', 'Suzie'],
    'Age': [27, 34, 21, 31],
    'Profession': ['Data Scientist', 'Software Developer','Graphic Designer','Project Manager']

}

st = pd.DataFrame(student)
print(st)
print()
print(st['Name'])
print()
print(st.Age)
print()
print(st.Profession)
print()
print(st.iloc[0])
print()
print(st['Name'][0])
print()
print(st[['Name','Profession']])

# 3. Loading Data into a DataFrame
import pandas as pd

path = r'C:\Users\User\Desktop\CSV\data.csv'
df = pd.read_csv(path)
#df = pd.read_csv(path, nrows=3)

print(df)
few_rows = df.head(3) 
print()  
print(few_rows)
print() 
print(df.dtypes)
print() 
print(df.describe())