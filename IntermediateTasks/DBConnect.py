"""Demo of connecting to a database."""

import MySQLdb

db = MySQLdb.Connect(host="pythonexample.ctemptlenqx0.eu-west-2.rds.amazonaws.com", user="root", passwd="Pa$$w0rd", db="movies")

cur = db.cursor()



uid = input("Insert your userID ")

cur.execute("SELECT * FROM users where id =", uid)
row= int(0)
for row in cur.fetchall():
    print("The Data is:", row[0])
db.close
