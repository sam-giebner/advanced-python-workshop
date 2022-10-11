# -*- coding: utf-8 -*-

# Import modules
import csv

# Define classes and functions
def csv_to_dict(csv_path):
    """
    Reads a CSV file and returns the rows as 
    a list of Python dictionaries.

    Parameters:
    csv_path: (string) Path to input csv.

    Returns:
    list: CSV rows as a list of Python dictionaries.
    """

    # Ensure that a csv path was povided
    if not csv_path:
        return

    # Open csv file
    with open(csv_path) as csv_file:
        
        # Create dict reader object
        csv_reader = csv.DictReader(csv_file)
        
        # Extract records from csv reader
        return [row for row in csv_reader]

def dict_to_csv(csv_path, headers_list, data_list):
    """
    Takes list of Python dictionaries and writes to
    a CSV file.

    Parameters:
    csv_path: (string) Output CSV file path.
    headers_list: (list) List of column headers.
    data_list: (list) List of python dictionaries.

    Returns:
    Nothing
    """

    # Ensure that a csv path, list of headers, and data list were provided
    if not csv_path or not data_list:

        # Exit function because required parameters were not provided
        return

    # Determine if a headers list was provided
    if not headers_list:

        # Derive headers from dict keys
        headers_list = data_list[0].keys()
    
    # Create output csv
    with open(csv_path, 'wb') as csvfile:

        # Create dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=headers_list)

        # Write column headers
        writer.writeheader()

        # Iterate through summary data
        for row in data_list:
            
            # Write row to csv
            writer.writerow(row)

if __name__ == '__main__':
    # This code executes when the file is run as a script
    
    # Data for testing the dict_to_csv function
    test_data = [
        {'Country':'Canada','Language':'English'},
        {'Country':'Brazil','Language':'Portuguese'},
        {'Country':'Ecuador','Language':'Spanish'}]

    # Test the dict_to_csv function
    dict_to_csv(
        csv_path = 'TestExport.csv',
        headers_list = None,
        data_list = test_data)