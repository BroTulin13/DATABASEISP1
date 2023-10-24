import mysql.connector
mydb=mysql.connector.connect(host="hostname", user="user1", password="pass", database="test1")
mycursor=mydb.cursor()
mycursor.execute(CREATE TABLE table1(id int, name varchar(255)))
mycursor=mydb.cursor()
sql="INSERT INTO table1(name, address)VALUES(%s, %s)"
val=("Stas","32st")
mysql.execute(sql,val)
mydb.commit()
sqltest_select_query="SELECT*FROM sqltest1db_developers"
cursor.execute(sqltest_select_query)
table1=cursor.fetchall()
print("Всего строк:", len(table1))
print("Вывод каждой строки")
for row in table1:
print("id",row[0])
print("address", row[1])
print("name", row[2])
cursor.close()
mycursor=mydb.cursor()
sql="UPDATE table1 SET address='32st'WHERE address='new1st'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")