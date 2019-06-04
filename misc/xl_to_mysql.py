import openpyxl
import datetime
import mysqlhelper

query = f"INSERT INTO opslag (datum, beschikbaar) VALUES (%s,%s)"
xl = 'W:/03_Ondersteuning/03_03_ICT/Prive/Infra/Storage/W-schijf-storage-afname.xlsx'

# returns list of tuples
def acquire_insert_data():
  # laad werkboek
  doc = openpyxl.load_workbook(xl)    
  # laad sheet
  sheet = doc['Plot']
  # kolom C: datums
  col_c = sheet['C']
  # kolom D: % vrij
  col_d = sheet['D']
  for cell in col_c:
    print(cell)

acquire_insert_data()
