import pymysql

class MySqlHelper:
  def __init__(self, host, user, password, db):
    self.host = host
    self.user = user
    self.password = password
    self.db = db    
    self.connect()
    self.sql = ""

  def connect(self):
    self.conn = pymysql.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      db=self.db
    )

  def execute_query(self, sql):
    self.sql = sql
    try:
      self.conn.cursor().execute(sql)
      self.conn.commit()
    except pymysql.MySQLError as e:
      print(e.args)

'''
mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')
mysql_helper.connect()
sql = (
  "INSERT INTO pydb.links (descript, url) "
  "VALUES ('testlinkie ETION', 'https://www.etion.be')"
)
mysql_helper.execute_query(sql)
'''