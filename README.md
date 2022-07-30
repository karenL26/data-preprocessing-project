# Data Preprocessing Project

In this project I work with the New York Airbnb data from Kaggle.com This data was downloaded from this [link](https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv).

[Here](src/explore.ipynb) you can find the exploratory data analysis maded to find patterns and get insights from the data.

And [here](src/app.py) you can find the final cleaning process, where the the pipeline that cleans the data is created.

## About the cleaning process:

The goal was to obtain a pipeline that cleans the data, in order to use it for future price prediction.
To obtain this pipeline, the following was done:
* The irrelevant columns were dropped.
* In the column reviews_per_month the missing values were replaced with 0.0
* The categorical variables were codificated
* The listing with price least or equal than 0 were removed.

Finally the pipeline was saved in cvs file.
