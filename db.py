import mysql.connector
def BaseDeDatos():
    conexion1=mysql.connector.connect(
        host="localhost",
        user="br1", 
        passwd="0724-852933bruno", 
        database="taller_moto")
    return conexion1

def show_reparaciones():
    conexion = BaseDeDatos()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('''
        SELECT r.id, r.patente, r.fecha_ingreso, r.fecha_egreso, r.descripcion, r.presupuesto, r.estado, c.nombre_apellido
        FROM reparaciones r
        JOIN vehiculos v ON r.patente = v.patente
        JOIN clientes c ON v.patente = c.vehiculo_patente;
    ''')
    result_query = cursor.fetchall()
    cursor.close()
    conexion.close()
    return result_query

def insert_reparaciones(patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado):
    conexion = BaseDeDatos()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('''INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
            VALUES (%s, %s, %s, %s, %s, %s)''', (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado))
    conexion.commit()  
    cursor.close()
    conexion.close()
    return

def editar_reparacion(id, patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado):
    conexion = BaseDeDatos()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('''
        UPDATE reparaciones
        SET patente = %s, fecha_ingreso = %s, fecha_egreso = %s, descripcion = %s, presupuesto = %s, estado = %s
        WHERE id = %s
    ''', (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado, id))
    conexion.commit()  
    cursor.close()
    conexion.close()
    return

def eliminar_reparacion(id):
    conexion = BaseDeDatos()
    cursor = conexion.cursor(dictionary=True)
    
    cursor.execute('''
        DELETE FROM reparaciones
        WHERE id = %s
    ''', (id,))
    
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def registrar_usuario(nombre_usuario, contraseña_hasheada):
    conexion = BaseDeDatos()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre_usuario, contraseña)
        VALUES (%s, %s)
    ''', (nombre_usuario, contraseña_hasheada))
    conexion.commit()
    cursor.close()
    conexion.close()
