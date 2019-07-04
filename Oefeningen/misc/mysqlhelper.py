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
    '''PERFORM A SELECT
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
      # print(f"Geaffecteerde rijen: {num_rows}") # DEBUG
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
      # print(f"Geaffecteerde rijen: {self.conn.affected_rows()}") # DEBUG
      self.conn.close()

  def execute_in_bulk(self, sql, args=None):
    '''OTHER THEN SELECT
    '''
    try:
      self.sql = sql
      self._connect()
      with self.conn.cursor() as cursor:
        cursor.executemany(sql, args)
        self.conn.commit()
    except pymysql.OperationalError as e:
      print(e.args)
    except pymysql.MySQLError as e:
      print(e.args)
    else:
      # print(f"Geaffecteerde rijen: {self.conn.affected_rows()}") # DEBUG
      self.conn.close()
