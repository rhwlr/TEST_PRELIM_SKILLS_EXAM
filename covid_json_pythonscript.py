import json
import csv

with open('covid_cases.json', 'r') as json_file: 
    covid_json = json.load(json_file)

with open('parsed_covid_cases.csv', 'w') as write_to_csv:
    csv_file = csv.writer(write_to_csv)
    csv_file.writerow(["dateRep", "countriesAndTerritories", "cases", "deaths"])

    for parse in covid_json['records']:
        csv_file.writerow([parse["dateRep"], parse["countriesAndTerritories"], parse["cases"], parse["deaths"]])



