# Notes for Chapter 2
# 2. Starting with Data

# Start by activating the environment
# Go to terminal: source carpe/bin/activate

# Import Libraries ------
import pandas as pd

# Read CSV using pandas ----
surveys_df = pd.read_csv("data/raw/surveys.csv")

surveys_df

# Exploring a dataframe & its attributes ----
surveys_df.head() # head
type(surveys_df) # type of the object
surveys_df.dtypes # types for each of the columns

surveys_df.columns # prints the column names
surveys_df.shape # rows x columns
surveys_df.head(15) # first 15 rows (0th through 14th)
surveys_df.tail(15)

# Getting the unique values
pd.unique(surveys_df['species_id']) # unique values in species_id column

site_names = pd.unique(surveys_df['plot_id'])
site_names.shape # 24 unique rows
len(site_names) # 24
surveys_df['plot_id'].nunique() # get the unique values without creating intermediate

# Groups in pandas -----
# Get a bunch of summary stats for a given column
surveys_df['weight'].describe() 

# Extract one by one
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()

# Can also summarize by variables
grouped_data = surveys_df.groupby('sex')
grouped_data.describe()
grouped_data.mean(numeric_only = True)

# Challenge:
grouped_data2 = surveys_df.groupby(['plot_id','sex'])
grouped_data2.mean(numeric_only = True)
surveys_df.groupby(['plot_id'])['weight'].describe()

# Quickly creating summary counts in pandas
# Count number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()

