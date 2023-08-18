# 1st Method

# Database of both local and cloud are present in file
# not to use excel as it can't have 10 million rows (limitation of 1,048,576 rows)
# i tried using it with 10 million rows of random data(each file of size 500 MB approx) working fine
# since i have to upload on github therefore used a correct not random data 
# to run the below code on visual studio download the local_data.txt and cloud_data.txt on the desktop
# if want to run on google colab simply upload both the files

def read_data_from_file(filename):
    data = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(": ", 1)  # Split into two parts only
            if len(parts) == 2:
                table_name, record = parts
                data.setdefault(table_name, []).append(eval(record))
    return data

def compare_records(record1, record2):
    return record1 == record2

def compare_data(source_data, target_data):
    for table_name in source_data:
        source_records = source_data[table_name]
        target_records = target_data.get(table_name, [])

        if len(source_records) != len(target_records):
            print(f"Record count mismatch in table '{table_name}'.")
            return False

        for source_record, target_record in zip(source_records, target_records):
            if not compare_records(source_record, target_record):
                print(f"Data mismatch in table '{table_name}'.")
                return False

    return True

local_data = read_data_from_file("local_data.txt")
cloud_data = read_data_from_file("cloud_data.txt")

if compare_data(local_data, cloud_data):
    print("Data in the target file is the same as the original data in the source file.")
else:
    print("Data mismatch between the source and target files.")

