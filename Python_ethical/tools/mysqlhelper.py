import pymysql

class MySqlHelper:
  def __init__(self, host, user, password, db):
    self.host = host
    self.user = user
    self.password = password
    self.db = db
    self.sql = ""

  def _connect(self):    
    self.conn = pymysql.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      db=self.db
    )
    return self.conn if self.conn else None

  def fetch_data(self, sql, args=None):
    '''SELECT    
    '''
    self.sql = sql
    self._connect()
    cursor = self.conn.cursor()
    try:      
      num_rows = cursor.execute(sql, args)
    except pymysql.OperationalError as e:
      print(e.args)
    except pymysql.MySQLError as e:
      print(e.args)
    else:
      print(f"Geaffecteerde rijen: {num_rows}")
      results = cursor.fetchall()
      self.conn.close()
      return results

  def execute_query(self, sql, args=None):
    '''OTHER THEN SELECT
    '''
    self.sql = sql
    self._connect()
    try:
      with self.conn.cursor() as cursor:      
        cursor.execute(sql, args)
        self.conn.commit()
    except pymysql.OperationalError as e:
      print(e.args)
    except pymysql.MySQLError as e:
      print(e.args)
    else:
      print(f"Geaffecteerde rijen: {self.conn.affected_rows()}")
      self.conn.close()

mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')

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
sql = f"INSERT INTO links (descript, url) VALUES (%s,%s)"
extra_links = [
  ('Best description ever', 'https://mytest.be'),
  ('Worst description ever', 'https://othertest.be'),
  ('No description', 'https://thirdtest.be'),
  ('Best description ever', 'https://no-test.be'),
]

try:
  conn = mysql_helper._connect()
  cursor = conn.cursor()
  cursor.executemany(sql, extra_links)
  conn.commit()
  cursor.close()
  conn.close()
except Exception as e:
  print(e)
finally:
  print('THE END')