import csv

def load_csv(csv_path):
    
    if not csv_path:
        return

    with open(csv_path) as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        
        return [row for row in csv_reader]