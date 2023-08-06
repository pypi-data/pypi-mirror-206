import csv
import json

def csv_to_json(csv_path):
    """
    Reads a CSV file and transforms it into a JSON object.

    Parameters:
    - csv_path: str, the path to the CSV file

    Returns:
    - json_data: dict, the JSON object created from the CSV data
    """
    # Open the CSV file
    with open(csv_path, "r") as csv_file:
        # Read the CSV data
        csv_data = csv.DictReader(csv_file)

        # Create an empty list to store the CSV rows
        rows = []

        # Loop through each row of the CSV data
        for row in csv_data:
            # Add the row to the list
            rows.append(row)

    # Convert the list of rows to a JSON object
    json_data = json.dumps(rows)

    # Return the JSON object
    return json_data
