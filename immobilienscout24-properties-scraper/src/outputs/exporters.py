thonimport json
import csv

def export_data(properties):
    # Export to JSON
    with open('output_data.json', 'w') as json_file:
        json.dump(properties, json_file, indent=4)
    
    # Export to CSV
    with open('output_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=properties[0].keys())
        writer.writeheader()
        writer.writerows(properties)