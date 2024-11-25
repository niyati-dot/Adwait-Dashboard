import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'niya'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

