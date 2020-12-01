# importar modulo
import sqlite3

# conexion
conexion = sqlite3.connect("pruebas.db")

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "titulo varchar (255), " +
               "description text, " +
               "precio int(255)" +
               ")")

# guardar cambios automaticamente
conexion.commit()

# insertar datos en la base de datos
cursor.execute(
    "INSERT INTO productos VALUES(null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("Precio:", producto[3])
    print("\n")

# imprime el primer producto
producto = cursor.fetchone()
print(producto)

# borrar todos los registros de la base de datos
#cursor.execute("DELETE FROM productos")
# conexion.commit()

# insertar muchos registros de una vez
productos = [
    ("ordenador portatil", "buen pc", 700),
    ("telefono portatil", "buen telefono", 140),
    ("placa madre", "buena placa", 80),
    ("tablet 15", "buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# cerrar conexion
conexion.close()
