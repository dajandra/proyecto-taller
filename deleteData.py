import sqlite3

conn = sqlite3.connect('taller_motos.db')
cursor = conn.cursor()

# Borrar registros de la tabla reparaciones
cursor.execute("DELETE FROM reparaciones")

# Borrar registros de la tabla vehiculos
cursor.execute("DELETE FROM vehiculos")

# Borrar registros de la tabla clientes
cursor.execute("DELETE FROM clientes")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()