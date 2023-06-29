import pymysql

dbConfig = {
     'user': 'root',  # use your admin name
     'password': "Pass",  # use your admin password
     'host': 'mysql',  # IP address of localhost
     'database': 'adlogin', # your databse
}

conn = pymysql.connect(**dbConfig)
print(conn)
