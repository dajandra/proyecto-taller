import sqlite3

conn = sqlite3.connect('taller_motos.db')
cursor = conn.cursor()

# Borrar tabla reparaciones
cursor.execute("DROP TABLE reparaciones")

# Borrar tabla vehiculos
cursor.execute("DROP TABLE vehiculos")

# Borrar tabla clientes
cursor.execute("DROP TABLE clientes")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()