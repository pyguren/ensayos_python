import mysql.connector


# conectar base de datos mysql con python
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)

# Confirmar que la conexion quede ok
# print("Conexión correcta")


# Crear una base de datos


cursor = database.cursor(buffered=True)
# buffered = true se utiliza cuando se esta haciendo muchas modificaciones a cursor y asi no entre en error

"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# mostrar base de datos
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# CRear tablas
cursor.execute("""
               CREATE TABLE IF NOT EXISTS vehiculos(
                   id int(10)auto_increment not null,
                   marca varchar(40) not null,
                   modelo varchar(40)not null,
                   precio float(10, 2) not null,
                   CONSTRAINT pk_vehiculo PRIMARY KEY(id)
               )
               """)

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# agregar informacion a las tablas

# cursor.execute("INSERT INTO vehiculos VALUES (NULL, 'opel', 'Astra', 18500)")

# agregar informacion de forma mas masiva

coches = [
    ('Mercedez', 'Clase C', 35000),
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000)

]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

# mostrar la informacion que esta en la tabla

#cursor.execute("SELECT * FROM vehiculos")
#cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000")
# cursor.execute(
#   "SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
"""
result = cursor.fetchall()

print("----Estos son mis coches----")


for coche in result:
    print(coche)
"""
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)


# borrar informacion de la base de datos
cursor.execute("DELETE FROM vehiculos WHERE marca ='Renault'")
database.commit()

print(cursor.rowcount, "borrados!!!")

# cambiar o actualizar informacion existente en la base de datos (modificar)

cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit()

print(cursor.rowcount, "Actualizados!!!")
