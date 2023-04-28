from extract import extract_data
import pandas as pd

def transform_data(data):
    # remove unnecessary column
    data.drop(data.iloc[:, 2:44], inplace=True, axis=1)

    # remove missing values:
    data_clean = data.dropna()   

    #round consumption values to the nearest integer
    data_column_name = data_clean.columns[-1]
    consumption_data = round(data_clean[data_column_name], 2)

    new_consumption_data = {
        data_column_name : consumption_data
    }

    new_consumption_dataframe = pd.DataFrame(new_consumption_data)
    data_clean= data_clean.drop([data_column_name], axis = 1)

    data_new = data_clean.join(new_consumption_dataframe)
    
    return data_new