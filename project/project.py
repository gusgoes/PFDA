import pandas as pd

# Load the data

weatherdata = pd.read_csv('C:\Users\gusgo\PFDA\PFDA\project\weatherreadings2.csv')  # read the data from the csv file

# Display the first few rows of the dataframe
weatherdata.head()