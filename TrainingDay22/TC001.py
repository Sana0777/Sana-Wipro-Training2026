import mysql.connector

host="localhost"
user="root"
password="root"
database="wipro2026"

connection=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor=connection.cursor()
print("Connected to MySQL database")

query="SELECT * FROM wipro2026.employee;"

cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)