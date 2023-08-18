# 2nd Method
# Directly fetching data from the database and comparing
# you should have actual connection to run the program and also the data should be present 
# install two package to run 
# pip install mysql
# pip install mysql-connector-python

import mysql.connector
from itertools import zip_longest

local_db_connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="local_database"
)

cloud_db_connection = mysql.connector.connect(
    host="cloud_host",
    user="username",
    password="password",
    database="cloud_database"
)

def batched_fetch_records(connection, table_name, batch_size=10000):
    cursor = connection.cursor(dictionary=True)
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

def compare_records(record1, record2):
    return record1 == record2

def compare_data(local_connection, cloud_connection):
    table_names = ["table1", "table2"]  # Says these are the table's name

    for table_name in table_names:
        local_records_gen = batched_fetch_records(local_connection, table_name)
        cloud_records_gen = batched_fetch_records(cloud_connection, table_name)

        for local_batch, cloud_batch in zip_longest(local_records_gen, cloud_records_gen):
            if len(local_batch) != len(cloud_batch):
                print(f"Record count mismatch in table '{table_name}'.")
                return False

            for local_record, cloud_record in zip(local_batch, cloud_batch):
                if not compare_records(local_record, cloud_record):
                    print(f"Data mismatch in table '{table_name}'.")
                    return False

    return True

if compare_data(local_db_connection, cloud_db_connection):
    print("Data in the target database is the same as the original data in the source database.")
else:
    print("Data mismatch between the source and target databases.")
