import csv

with open("scripts/csv-test.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # uses the first line as headers and the rest as values, Reads each row as a dict
    for row in reader:
        print(row)

