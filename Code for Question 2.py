# Note : You can run the code in Jupyter notebook, Google Colab or visual studio
# first install two package
# pip install mysql
# pip install mysql-connector-python


import mysql.connector 

# Sample data representing the local database
local_data = {
    "table1": [
        {"id": "1", "name": "John", "age": "30"},
        {"id": "2", "name": "Alice", "age": "25"}
    ],
    "table2": [
        {"id": "101", "address": "123 Main St", "city": "New York"},
        {"id": "102", "address": "456 Oak Ave", "city": "Los Angeles"}
    ]
}

# Sample data representing the cloud database (AWS or GCP)
cloud_data = {
    "table1": [
        {"id": "1", "name": "John", "age": "30"},
        {"id": "2", "name": "Alice", "age": "25"}
    ],
    "table2": [
        {"id": "101", "address": "123 Main St", "city": "New York"},
        {"id": "102", "address": "456 Oak Ave", "city": "Los Angeles"}
    ]
}

def compare_table_data(source_data, target_data, table_name):
    source_records = source_data.get(table_name, [])
    target_records = target_data.get(table_name, [])

    # Compare record counts
    if len(source_records) != len(target_records):
        print(f"Record count mismatch in table '{table_name}'.")
        return False

    # Compare each record in the table
    for source_record, target_record in zip(source_records, target_records):
        if source_record != target_record:
            print(f"Data mismatch in table '{table_name}'.")
            return False

    return True

def compare_data(source_data, target_data):
    # Compare table names
    source_tables = set(source_data.keys())
    target_tables = set(target_data.keys())

    if source_tables != target_tables:
        print("Table structure mismatch between source and target databases.")
        return False

    # Compare data in each table
    for table_name in source_tables:
        if not compare_table_data(source_data, target_data, table_name):
            return False

    return True

# Test the data consistency
if compare_data(local_data, cloud_data):
    print("Data in the target database is the same as the original data in the source database.")
else:
    print("Data mismatch between the source and target databases.")







