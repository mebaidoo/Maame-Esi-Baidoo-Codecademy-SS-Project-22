import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
#Inspecting the dataframe
print(census.head())
print(census.dtypes)
print(census.birth_year.unique())
#Replacing "missing" values in the birth_year column with 1967 and changing the data type of the column to int
census["birth_year"].replace("missing", 1967, inplace = True)
census["birth_year"] = census["birth_year"].astype("int")
print(census.birth_year.unique())
print(census.dtypes)
#Finding the average birth_year
print(census.birth_year.mean())
#Converting the higher_tax variable to category data type
census["higher_tax"] = pd.Categorical(census["higher_tax"], ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"], ordered = True)
print(census.higher_tax.unique())
#Label encoding the higher_tax variable and finding its median value
census["higher_tax"] = census.higher_tax.cat.codes
print(census.head())
print(census.higher_tax.median())
#One Hot Encoding the marital_status variable
census = pd.get_dummies(data = census, columns = ["marital_status"])
print(census.head())