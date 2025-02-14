import json
import csv

# Read JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)  # Load JSON data

# Convert JSON to CSV
csv_file = "output.csv"
with open(csv_file, "w", newline="") as csvfile:
    fieldnames = data[0].keys()  # Extract column names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write column headers
    writer.writerows(data)  # Write data rows

print(f"CSV file '{csv_file}' has been created.")
