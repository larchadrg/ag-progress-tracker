import csv
import json

# Specify the paths for input CSV and output JSON files
csv_file_path = 'characters.csv'
json_file_path = 'output_data.json'

# Read data from CSV file
data = []
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        data.append(row)

# Write data to JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=2)

print(f"Data has been converted to {json_file_path}")
