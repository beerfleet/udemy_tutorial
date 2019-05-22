from projects.mysqlhelper import MySqlHelper
import pymysql

# EXAMPLE SELECT
# mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')
# sql = ("SELECT * FROM pydb.links")
# results = mysql_helper.fetch_data(sql)
# print(results)

# EXAMPLE QUERY BEST WAY
# descript = 'Some description here ...'
# url = 'etion'
# pattern = f"%{url}%"
# sql = f"SELECT * FROM links WHERE url like %s"
# results = mysql_helper.fetch_data(sql, (pattern,))
# print(results)

# INSERT EXAMPLE WITH PREPARED STATEMENT
# insert_data = ('1111', 'Some other lame description', 'http://maduro.burro.vz')
# sql = f"INSERT INTO links (descript, url) VALUES (%s,%s)"
# mysql_helper.execute_query(sql, insert_data)

#INSERT IN BULK
mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')
sql = f"INSERT INTO links (descript, url) VALUES (%s,%s)"
extra_links = [
  ('Best description ever', 'https://mytest.be'),
  ('Worst description ever', 'https://othertest.be'),
  ('No description', 'https://thirdtest.be'),
  ('Best description ever', 'https://no-test.be'),
]

try:
  conn = mysql_helper._connect()  
  with conn.cursor() as c:
    c.executemany(sql, extra_links)
    conn.commit()
    c.close()

except pymysql.OperationalError as op_err:
  print(op_err)
except pymysql.DatabaseError as db_err:
  print(db_err)
except Exception as err:
  print(err)
finally:
  print('THE END')
    