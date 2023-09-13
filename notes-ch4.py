# Notes from Chapter 4
# 4. Indexing, slicing, and subsetting dataframes in python

# Import pandas
import pandas as pd

# Read the survey data
surveys_df = pd.read_csv('data/raw/surveys.csv')

# Create a list of the survey species
survey_species = surveys_df['species_id']

# Select subsets
surveys_df[0:3] # selects 0, 1, 2 (first 3 rows)
surveys_df[:5] # selects first 5 rows
surveys_df[-1:] # selects last element

# Copying vs Referencing -----------------------------
# Copy creates a complete new copy
true_copy_surveys_df = surveys_df.copy()

# Referencing creates a new variable referencing the same object
# (e.g. no new copy will be made)
ref_surveys_df = surveys_df

# Reassigning values within a reference
ref_surveys_df[0:3] = 0

# Now the original data is going to be different
true_copy_surveys_df.head()
surveys_df.head()

# Create a new clean dataframe from the original file ----
surveys_df = pd.read_csv("data/raw/surveys.csv")

# Slicing subsets of rows and columns
# iloc: integer based indexing from 0
surveys_df.iloc[0:3, 1:4] 

# loc: label based indexing by names
surveys_df.loc[[0, 10], :] # select all columns for rows of index values 0 and 10
surveys_df.loc[0, ['species_id', 'plot_id', 'weight']] # select 0th row and those three cols
surveys_df.loc[[0, 10, 35549], :] # last row is index n-1

# Can find a specific data element using dat.iloc[row, column]
surveys_df.iloc[2, 6]


# Range
surveys_df[0:1] # just shows first row
surveys_df[0] # error
surveys_df[:4] # first 4 rows
surveys_df[:-1] # everything except last row

surveys_df.iloc[0:1] # just shows first row
surveys_df.iloc[0] # first row as named list
surveys_df.iloc[:4, :] # first 4 rows
surveys_df.iloc[0:4, 1:4] # specified cols of first 4 rows
surveys_df.loc[0:4, 1:4] # error: need to use labels


# Subset data with criteria ---------
surveys_df[surveys_df.year == 2002] # select all rows where year is 2002
surveys_df[surveys_df.year != 2002] # select all rows where year is NOT 2002
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)] # between 1980-1985

# Avaliable syntax
# Equals: ==
# Not equals: !=
# Greater than, less than: > or <
# Greater than or equal to >=
# Less than or equal to <=

# Challenge:
# Subset for Year == 1999 and Weight <= 8
surveys_df[(surveys_df.year == 1999) & (surveys_df.weight <= 8)] # 5 rows

# Use mask to identify condition
# Sex x to 5
x = 5

# Now try:
x > 5 # false
x == 5 # true

pd.isnull(surveys_df) # will show whether data is null

# Select rows where there are null values
surveys_df[pd.isnull(surveys_df).any(axis=1)]

# 
empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
print(empty_weights)

# selection of the data with isin
stack_selection = surveys_df[(surveys_df['sex'].isin(['M', 'F'])) &
              surveys_df["weight"] > 0.][["sex", "weight", "plot_id"]]

# calculate the mean weight for each plot id and sex combination:
stack_selection = (stack_selection
                   .groupby(["plot_id", "sex"])
                   .mean()
                   .unstack())

# and we can make a stacked bar plot from this:
stack_selection.plot(kind='bar', stacked=True)