import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
mysql_database = argv[3]
state_name     = argv[4]


dbconnect = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=mysql_database)

cursor = dbconnect.cursor()


cursor.execute("SELECT name FROM cities WHERE state_id = (SELECT id  FROM states WHERE BINARY  name = %s) ", [state_name])
cities = cursor.fetchall()

for i, city in enumerate(cities):
    print(city[0], end=', ' if i < len(cities)-1 else '\n')
if not cities:
    print('')

# Close all cursors
cursor.close()
# Close all databases
dbconnect.close()
