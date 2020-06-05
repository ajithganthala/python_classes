import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",password="root",db="college")
cur=con.cursor()
cur.execute("select * from clgdata")
result=cur.fetchall()
print("The clg id\n college name\n no_of_students\n ",result)
