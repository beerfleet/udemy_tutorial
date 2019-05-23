from projects.mysqlhelper import MySqlHelper
import pymysql


def provide_credentials():
    username = input(f"Please provide your username: ")
    password = input(f"Please provide your pasword: ")
    return (username, password,)

def check_creds(creds):
    mysql_helper = MySqlHelper('localhost', 'root', '', 'pydb')
    sql = '''
        SELECT * FROM user
        WHERE username=%s
        AND password=%s
    '''
    sql = sql.replace('\n', '')
    return mysql_helper.fetch_data(sql, creds)
    

if __name__ == "__main__":    
    creds = provide_credentials()
    if check_creds(creds):
        print(f"Welcome, {creds[0]}")
    else:
        print(f"Bad credentials")