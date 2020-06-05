import MySQLdb

def  getDbConnection():
    try:
        con=MySQLdb.connect(host="localhost",user="root",passwd="root",db="college")
        return(con)
    except:
        print("Start my sql")

def  getDbConnections():
    try:
        cur=cont.cursor()
        print('Database is successfully Connected')
        print()
        return(cur)
    except:
        print("Start db connection")
def closeDbConnection():
    curs.close()
    cont.close()
    print("The database is disconnected")
    print()

def printDbVersion():
    print("the database version is : ",cont.get_server_info())
    print()


def readCollegeDetails(college_id):
    curs.execute("select * from clgdata where clg_id=%s",[college_id] )
    result=curs.fetchone()
    print()
    print("Printing the college record according to the given ID:")
    print()
    for i in range(len(result)):
        print("clg_id=%s\n clg_name=%s\n no_of_students=%s\n",[result[i]])
    print()

def readProfessorDetails(professor_id):
    curs.execute("select * from profdata where prof_id=%s",[professor_id])
    result=curs.fetchone()
    print()
    print("Printing the professor record according to the given ID: ")
    print()
    for j in range(len(result)):
        print(result[j])
    print()
   
print("Started python data base execution program with MySQLdb")
print("-------------------------**********--------------------------------")
print()
cont=getDbConnection()
curs=getDbConnections()
printDbVersion()
n=int(input("Enter Colldge Id to search and get the details: "))
readCollegeDetails(n)
closeDbConnection()
cont=getDbConnection()
curs=getDbConnections()
m=int(input("Enter the professor ID to search and get the details : "))
readProfessorDetails(m)
closeDbConnection()
print("-------------------------**********--------------------------------")
print("Ended python data base execution program with MySQLdb")
