from tabulate import tabulate
import os
import csv

print(os.listdir())

csvs = []
for file in os.listdir("Datos\Impares"):
    print(file)
    csvs.append(file)
for archivo_csv in csvs:
    with open(f'Datos\\Impares\\{archivo_csv}', encoding="Latin-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
    print("")
    