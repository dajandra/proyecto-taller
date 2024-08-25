import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('taller_motos.db')
cursor = conn.cursor()

# Crear registros de ejemplo para la tabla clientes
cursor.execute("INSERT INTO clientes (nombre_apellido, telefono, domicilio, vehiculo_patente) VALUES (?, ?, ?, ?)",
               ('Juan Pérez', '123456789', 'Calle 1', 'ABC123'))
cursor.execute("INSERT INTO clientes (nombre_apellido, telefono, domicilio, vehiculo_patente) VALUES (?, ?, ?, ?)",
               ('María González', '987654321', 'Calle 2', 'DEF456'))
cursor.execute("INSERT INTO clientes (nombre_apellido, telefono, domicilio, vehiculo_patente) VALUES (?, ?, ?, ?)",
               ('Pedro Rodríguez', '555123456', 'Calle 3', 'GHI789'))

# Crear registros de ejemplo para la tabla vehiculos
cursor.execute("INSERT INTO vehiculos (patente, modelo, año) VALUES (?, ?, ?)",
               ('ABC123', 'Toyota Corolla', 2015))
cursor.execute("INSERT INTO vehiculos (patente, modelo, año) VALUES (?, ?, ?)",
               ('DEF456', 'Ford Focus', 2018))
cursor.execute("INSERT INTO vehiculos (patente, modelo, año) VALUES (?, ?, ?)",
               ('GHI789', 'Honda Civic', 2020))

# Crear registros de ejemplo para la tabla reparaciones
cursor.execute("INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado) VALUES (?, ?, ?, ?, ?, ?)",
               ('ABC123', '2022-01-01', '2022-01-15', 'Cambio de aceite', 500.0, 'sin empezar'))
cursor.execute("INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado) VALUES (?, ?, ?, ?, ?, ?)",
               ('DEF456', '2022-02-01', '2022-02-20', 'Reparación de frenos', 800.0, 'en proceso'))
cursor.execute("INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado) VALUES (?, ?, ?, ?, ?, ?)",
               ('GHI789', '2022-03-01', '2022-03-25', 'Revisión general', 1000.0, 'finalizado'))

# Commit y cerrar la conexión
conn.commit()
conn.close()