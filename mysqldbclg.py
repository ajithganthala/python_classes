def getdbconnection():
    import MySQLdb
    con=MySQLdb.connect(host="localhost",user="root",password="root",db="college")
    cur=con.cursor()

def closedbconnection():
    con.connect()
    con.close()

def printdbversion():
    print("Version of database is : ",con.get_server_info())

def readcollegedetails(college_id):
    cur=con.cursor()
    cur.execuitve("select * from clgdata")
    result=cur.fetchall()
    print(result)

def readprofessordetails(prof_id):
    cur=con.cursor()
    cur.executive('select * from profdata')
    result=cur.fetchall()
    print(result)

getdbconnection()
closedbconnection()
printdbversion()
