import openpyxl
import datetime
import time
from mysqlhelper import MySqlHelper

query = f"INSERT INTO opslag (datum, beschikbaar) VALUES (%s,%s)"
xl = 'W:/03_Ondersteuning/03_03_ICT/Prive/Infra/Storage/W-schijf-storage-afname.xlsx'

# returns list of tuples
def acquire_insert_data():
  # laad werkboek
  doc = openpyxl.load_workbook(xl, data_only=True)
  # laad sheet
  sheet = doc['Plot']
  # kolom C: datums
  col_c = sheet['C']
  # kolom D: % vrij
  col_d = sheet['D']
  return [(datetime.datetime(el[0].value).strftime('%Y-%m-%d'), el[1].value) for el in zip(col_c, col_d)]


if __name__ == "__main__":
  insert_data = acquire_insert_data()
  print(insert_data)
  # mysql = MySqlHelper('localhost', 'root', '', 'pydb')
  # mysql.execute_query(query, insert_data)