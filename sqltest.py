#connecting to our azure database and making a SQLquery
#brew install unixodbc
import pyodbc
server = 'upliftedu.database.windows.net'
database = 'UpliftEdu'
username = 'Hack2020'
password = 'UpliftEdu1'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * from StudentInfo;")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1])+ " " + str(row[2])+ " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
    row = cursor.fetchone()