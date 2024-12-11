import getpass
import oracledb

# pw = getpass.getpass("Enter password: ")
oracledb.init_oracle_client(lib_dir = "C:\instanclient\instantclient_19_25")

connection = oracledb.connect(
    user="AMR",
    password="AMR",
    dsn = "10.124.12.2:1521/db1p"
    )

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a table

cursor.execute("SELECT * FROM CALENDAR")

for row in cursor:
    print(row)

cursor.close()
connection.close()
