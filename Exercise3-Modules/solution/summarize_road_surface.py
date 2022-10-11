# -*- coding: utf-8 -*-

"""
Author(s): Sam Giebner
Date created: 10/10/2022
Date last modified: 10/11/2022
Python Version: 2 & 3
Run time: Dynamic
Description: Takes in a CSV of road data, 
totals the mileage by road surface type,
and outputs the totals as a CSV.
"""

# Import modules
import logging
from helpers import csv_tasks

# Define classes and functions
def summarize_road_data(surface_types, road_data):
    """
    Parses a list of Python dictionaries conatining
    road data and totals the mileage per surface type.

    Parameters:
    surface_types: (list) List of surface types.
    road_data: (list) List of dictionaries conatining road data.

    Returns:
    list: List of dictionaries containing mileage totals per surface type.
    """

    # Create list for storing summary data
    raw_summary_data = []

    # Iterate through surface types
    for surface in surface_types:

        # Create list of road segments that match the surface type
        surface_segments = [seg for seg in road_data if seg['SURF_TYPE'] == surface]

        '''
        Calculate total surface mileage by:
          1. Select road segments that have a mileage value
          2. Convert mileage value from string to float
          3. Sum the list of mileage values
        '''
        surface_miles = sum([float(seg['MILES']) for seg in surface_segments if seg['MILES']])

        # Create a temporary dict for storing stats
        surface_stats = {
            'Surface': surface,
            'Miles': surface_miles}

        # Append surface stats to summary data
        raw_summary_data.append(surface_stats)

    logging.info('Calculated total mileage by surface type.')

    # Sort raw summary data by total mileage
    summary_data = sorted(raw_summary_data, key=lambda d: d['Miles'], reverse=True)

    logging.info('Sorted surface types by total mileage.')

    return summary_data

def main():

    # Define input csv file
    input_csv = 'BeltramiCountyRoads.csv'

    # Define output csv file
    output_csv = 'Beltrami_RoadSurfaceSummary.csv'

    # Define log file name as script name, replacing .py with .log 
    log_file = __file__.replace('.py', '.log')

    print(log_file)

    # Create and configure logger
    logging.basicConfig(
        filename = log_file, # Define log file path
        format = '%(asctime)s %(message)s', # Add date/time to log messages
        filemode = 'w', # ‘w’ overwrites existing log and ‘a’ appends to existing log
        level = logging.DEBUG) # Set logger to record debug or higher

    # Add handler to print messages to terminal
    logging.getLogger().addHandler(logging.StreamHandler())

    try:

        # Load csv data a list of of dicts
        road_data = csv_tasks.csv_to_dict(input_csv)

        logging.info('Loaded features from CSV file.')

        '''
        Generate list of unique surface types by:
          1. Select values that are not Null using list comprehension
          2. Use set() create a unique set of values
          3. Use list() to convert set to list
        '''
        surface_types = set([seg['SURF_TYPE'] for seg in road_data if seg['SURF_TYPE']])

        logging.info('Generated unique list of road surface types.')

        # Summarize road data
        summary_data = summarize_road_data(surface_types, road_data)

        logging.info('Summarized road data.')

        # Export data to csv
        csv_tasks.dict_to_csv(
            csv_path = output_csv,
            headers_list = ['Surface', 'Miles'],
            data_list = summary_data)

        logging.info('Exported data to summary CSV.')

        # Record successful completion
        logging.info('Script successfully completed!')

    except:

        # Log error message
        logging.exception('Script failed!')

if __name__ == '__main__':
    main()