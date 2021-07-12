import MySQLdb

myConnection = MySQLdb.connect( host='103.212.120.142', user='Jala_python', passwd='Public@123', db='Jala_python')
cur = myConnection.cursor()
cur.execute('SELECT * FROM User')
print(cur.fetchall())
