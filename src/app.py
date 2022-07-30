import pandas as pd

# Reading de data
df_raw = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv")

#Creating a copy to clean de data
df_clean = df_raw.copy()

print("Droping the irrelevant columns")
df_clean.drop(['id','host_name', 'name', 'last_review'], axis=1, inplace=True)

print("Replacing the null values in reviews_per_month with 0.0")
df_clean['reviews_per_month'].fillna(0.0, inplace=True)

print("Codification of categorical variables")
# Encoding categorical data
df_clean = pd.get_dummies(df_clean, columns=['room_type'])
df_clean = pd.get_dummies(df_clean, columns=['neighbourhood_group'])
df_clean = pd.get_dummies(df_clean, columns=['neighbourhood'])

print("Droping listings with prices least or equal than 0")
df_clean = df_clean.loc[df_clean['price'] > 0]

print("Saving the pipeline in csv file")
df_clean.to_csv('data/processed/data_processed.csv')
