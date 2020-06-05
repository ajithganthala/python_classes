import MySQLdb
con=MySQLdb.connect(host="localhost",user="root", password="root",db="employee")
cur=con.cursor() #it will point the first line
"""n = input("Enter the employee_ID to search : ")
#a = input("Enter email id to update: ")
result = cur.execute("delete from employee_table where empid=%s",[n])
#result = cur.fetchone() #fetchall will take every thing in database
#for i in result:
 #   print(i)
print(result,"Records are deleted")
cur.close()
con.commit()
con.close()"""
