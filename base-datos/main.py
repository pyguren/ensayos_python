import mysql.connector


# conectar base de datos mysql con python
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)

print("Conexión correcta")


# Crear base de datos


cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# mostrar base de datos
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
