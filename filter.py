import csv
import re

def remove_special_characters(text):
    # Define a pattern to match special characters
    pattern = r'[^a-zA-Z0-9\s]'  # This pattern keeps alphanumeric characters and spaces

    # Use regex to substitute special characters with an empty string
    filtered_text = re.sub(pattern, '', text)
    
    return filtered_text

def filter_csv(Aprildata, filtereddata):
    with open(Aprildata, 'r', newline='') as infile, \
         open(filtereddata, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            filtered_row = [remove_special_characters(cell) for cell in row]
            writer.writerow(filtered_row)

    print(f"Filtered CSV data saved to '{filtereddata}'")

# Example usage:
input_csv_file = 'Aprildata.csv'
output_csv_file = 'filtereddata.csv'
filter_csv(input_csv_file, output_csv_file)
