# crear_base_de_datos.py
import sqlite3

conn = sqlite3.connect('taller_motos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_apellido TEXT NOT NULL,
        telefono TEXT,
        domicilio TEXT,
        vehiculo_patente TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE vehiculos (
        patente TEXT PRIMARY KEY,
        cliente_id INTEGER,
        modelo TEXT NOT NULL,
        año INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')

cursor.execute('''
    CREATE TABLE reparaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patente TEXT,
        fecha_ingreso DATE NOT NULL,
        fecha_egreso DATE,
        descripcion TEXT,
        presupuesto REAL,
        estado TEXT NOT NULL DEFAULT 'sin empezar',
        FOREIGN KEY (patente) REFERENCES vehiculos(patente)
    )
''')

conn.commit()
conn.close()