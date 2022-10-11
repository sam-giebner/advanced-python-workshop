from helpers import data_tasks

csv_data = data_tasks.load_csv(csv_path='Exercise3\solution\BeltramiCountyRoads.csv')

surface_types = list(set([i['SURF_TYPE'] for i in csv_data]))


for surface in surface_types:

    road_miles = sum([float(i['MILES']) for i in csv_data if i['SURF_TYPE'] == surface and i['MILES']])