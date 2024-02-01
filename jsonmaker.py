import csv
import json
import os
print(os.getcwd())

# os.chdir("/Users/vasanth/Desktop/Projects/ntufood")

# Define the path to the CSV file and the output JSON file
csv_file_path = 'data.csv'
json_file_path = 'storesData.json'

# Initialize an empty list to hold the converted JSON data
stores_data = []

# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    # Use the CSV DictReader to read the CSV file into a dictionary
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert the CSV row to a JSON object (dictionary)
        store = {
            "storeName": row["Name"],
            "location": row["location"],
            "vegetarian": True if row["has vegetarian options"].lower() == 'yes' else False,
            "openingHours": row["opening hours "]
        }
        stores_data.append(store)

# Write the JSON data to the output file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    jsonfile.write(json.dumps(stores_data, indent=4))

print(f"JSON data has been written to {json_file_path}")
