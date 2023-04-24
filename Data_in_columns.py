import requests
import json
import csv
from decouple import config



Api_name = "[API Request]"
Api_name2 = "[APIR-Request]"

token = "Api-Token " + config('[API_TOKEN]')
headers = {
    'Authorization': token
    }
    
responseHigh = requests.get(URL_DYNATRACE_HIGH_OPEN, headers=headers)
dataHigh = json.loads(responseHigh.text)

responseCritical = requests.get(URL_DYNATRACE_CRITICAL_OPEN, headers=headers)
dataCritical = json.loads(responseCritical.text)


with open('[File1.csv]', 'w', newline='') as file:
    writer = csv.writer(file)

    headers = ['header1', 'header2', 'header3']
    writer.writerow(headers)

    if 'variableX' in XXX:
        for item in XXX['variableX']:
            row = [item['Header1'], item['Header2'], item['Header3'],]
            writer.writerow(row)

    else:
        print("Error")

file.close()

with open('File_2', 'w', newline='') as file:
    writer = csv.writer(file)

    headers = ['Header1', 'Header2', 'Header3']
    writer.writerow(headers)

    if 'variableX' in XXX:
        for item in XXX['variableX']:
            row = [item['Header1'], item['Header2'], item['Header3']]
            'print(row)'
            writer.writerow(row)

    else:
        print("error")
file.close()

import pandas as pd
from openpyxl.utils import get_column_letter

# Pfad zur CSV-Datei
file_path = "File_2"

# DataFrame aus der CSV-Datei erstellen
df = pd.read_csv(file_path)

# Spalten in String umwandeln
df = df.astype(str)

# Anzahl der neuen Spalten berechnen
num_new_cols = df.iloc[:, 0].str.count(",") + 1

# Neue Spalten erstellen
new_cols = []
for i in range(num_new_cols.max()):
    new_col = df.iloc[:, 0].str.split(",", expand=True).iloc[:, i]
    new_cols.append(new_col)

# DataFrame mit neuen Spalten erstellen
new_df = pd.concat([df] + new_cols, axis=1)

# Ausgabe des neuen DataFrames
print(new_df.head())

# Pfad zur Excel-Datei
excel_path = "File_new_2.xlsx"

# DataFrame als Excel-Datei speichern
with pd.ExcelWriter(excel_path) as writer:
    new_df.to_excel(writer, index=False)
    # Spaltenbreite automatisch anpassen
    for column in writer.sheets['Sheet1'].columns:
        max_length = 0
        column_name = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        writer.sheets['Sheet1'].column_dimensions[column_name].width = adjusted_width