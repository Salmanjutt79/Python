import mysql.connector
mydb=mysql.connector.connect(host='local',user='root',password="Salman@123")
cur=mydb.cursor()
cur.execute("CREATE DATABASE student")
