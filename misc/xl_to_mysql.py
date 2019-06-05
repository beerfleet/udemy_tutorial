""" 
This imports data from the initial xl disk space shrinkage file
"""

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
  # str_col_c = [str(el.value) for el in col_c]
  # kolom D: % vrij
  col_d = sheet['D']
  # return str_col_c[1:]
  return [(str(el[0].value), str(el[1].value)) for el in zip(col_c, col_d)][1:]


if __name__ == "__main__":
  insert_data = acquire_insert_data()
  # print(insert_data)
  mysql = MySqlHelper('localhost', 'root', '', 'pydb')
  mysql.execute_in_bulk(query, insert_data)