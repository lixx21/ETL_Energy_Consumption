# import libraries
import pandas as pd

#read dataset:
def extract_data(file):
    data = pd.read_csv(file)
    
    return data

# data = extract_data('data\Energy Statistics\Consumption_Data\Consumption_Coal.csv')

# print(data.shape)