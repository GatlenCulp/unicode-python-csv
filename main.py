'''
/usr/local/bin/python3
main.py

Author: Gatlen Culp
Date: 19 June 2024

Description: This script generates a CSV file containing information about Unicode characters.
It iterates over a range of Unicode characters, retrieves their properties using the `unicodedata` module, and writes the information to a CSV file.
'''

#%% Imports
import csv
import unicodedata

#%% Main Code
# Define the file name for the CSV
output_file = "unicode_characters.csv"

# Define the range of Unicode characters
unicode_range = range(0x110000)  # Up to the last Unicode character

# Define the fields for the CSV
fields = [
    "Character",
    "Code",
    "Name",
    "Category",
    "Bidirectional Class",
    "Combining Class",
    "East Asian Width",
    "Numeric Value",
]

def main():
    # Open the CSV file for writing
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the header
        csvwriter.writerow(fields)

        # Iterate over the Unicode range
        for code in unicode_range:
            try:
                char = chr(code)
                name = unicodedata.name(char, "")
                category = unicodedata.category(char)
                bidirectional = unicodedata.bidirectional(char)
                combining = unicodedata.combining(char)
                east_asian_width = unicodedata.east_asian_width(char)
                numeric_value = unicodedata.numeric(char, "")

                row = [
                    char,
                    f"U+{code:04X}",
                    name,
                    category,
                    bidirectional,
                    combining,
                    east_asian_width,
                    numeric_value,
                ]

                # Write the row to the CSV
                csvwriter.writerow(row)

            except Exception as e:
                # Handle any exceptions (e.g., characters that are not defined)
                print(f"Error processing code {code}: {e}")

    print(f"CSV file '{output_file}' has been generated.")

#%% Run the main function
if __name__ == "__main__":
    main()