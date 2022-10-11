# -*- coding: utf-8 -*-

import csv
import logging

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

        # Open csv file
        with open(input_csv) as csv_file:
            
            # Create dict reader object
            csv_reader = csv.DictReader(csv_file)
            
            # Extract records from csv reader and store data as variable
            road_data = [row for row in csv_reader]

        logging.info('Loaded features from CSV file.')

        '''
        Generate list of unique surface types by:
        1. Select values that are not Null using list comprehension
        2. Use set() create a unique set of values
        3. Use list() to convert set to list
        '''
        surface_types = set([seg['SURF_TYPE'] for seg in road_data if seg['SURF_TYPE']])

        logging.info('Generated unique list of road surface types.')

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

        # Create output csv
        with open(output_csv, 'wb') as csvfile:

            # Define column headers
            headers = ['Surface', 'Miles']

            # Create dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=headers)

            # Write column headers
            writer.writeheader()

            # Iterate through summary data
            for row in summary_data:
                
                # Write row to csv
                writer.writerow(row)

        logging.info('Exported data to summary CSV.')

        # Record successful completion
        logging.info('Script successfully completed!')

    except:

        # Log error message
        logging.exception('Script failed!')

if __name__ == '__main__':
    main()