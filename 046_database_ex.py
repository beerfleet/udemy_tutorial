from Python_ethical.tools.mysqlhelper import MySqlHelper

if __name__ == "__main__":
    mysql = MySqlHelper('localhost', user='root', password='', db='')
    sql = ("SELECT * FROM pydb")
    mysql.execute_query(sql)
    