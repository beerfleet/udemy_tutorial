from projects.mysqlhelper import MySqlHelper
import pymysql

mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')
sql = '''
    SELECT * from pydb.links as l
    WHERE l.url like %s
'''
args = "%http%"
results = mysql_helper.fetch_data(sql, args)
for row in results:
    print(row)