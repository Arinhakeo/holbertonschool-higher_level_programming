#!/usr/bin/python3


import csv
import json

def convert_csv_to_json(csv_filename):
    try:

        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        return True

    except FileNotFoundError:
        print(f"Le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False
    
if __name__ == "__main__":
    csv_file = "data.csv"
    success = convert_csv_to_json(csv_file)
    if success:
        print(f"Les données de {csv_file} ont été converties en data.json.")
    else:
        print("La conversion a échoué.")
