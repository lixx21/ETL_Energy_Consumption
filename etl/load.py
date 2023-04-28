from extract import extract_data
from transform import transform_data
import psycopg2
import argparse

def load_data(file_path):

    connection = psycopg2.connect(database="energy_consumption",
                        host="localhost",
                        user="postgres",
                        password="123456",
                        port="5434")

    cursor = connection.cursor()

    print("loading data...")
    data = extract_data(file_path)

    print("transforming data...")
    data_transform = transform_data(data)

    column_name = data_transform.columns[-1]

    #create table
    query_create_table = f"CREATE TABLE IF NOT EXISTS {column_name}(\
    ID SERIAL PRIMARY KEY,\
    continent varchar(50) NOT NULL,\
    country varchar(50) NOT NULL,\
    {column_name} decimal\
    );"

    cursor.execute(query_create_table)

    #start loading data
    print('loading data...')
    for index, row in data_transform.iterrows():
        query_insert_value = f"INSERT INTO {column_name} (continent, country, {column_name}) VALUES ('{row[0]}', \
            '{row[1]}', {row[2]})" 
        
        cursor.execute(query_insert_value)
    connection.commit()

    cursor.close()
    connection.close()

    print("etl success...\n")

    return "all processes completed"

if __name__ == "__main__":

    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-f", "--file", help = "file path of your dataset")
    
    # Read arguments from command line
    args = parser.parse_args()

    load_data(args.file)
