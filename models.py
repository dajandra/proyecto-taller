# models.py
import sqlite3

class Reparacion:
    def __init__(self, id, patente, nombre_apellido, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado):
        self.id = id
        self.patente = patente
        self.nombre_apellido = nombre_apellido
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso
        self.descripcion = descripcion
        self.presupuesto = presupuesto
        self.estado = estado

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT r.id, r.patente, c.nombre || ' ' || c.apellido AS nombre_apellido, r.fecha_ingreso, r.fecha_egreso, r.descripcion, r.presupuesto, r.estado
            FROM reparaciones r
            JOIN vehiculos v ON r.patente = v.patente
            JOIN clientes c ON v.cliente_id = c.id
        ''')
        reparaciones = cursor.fetchall()
        conn.close()
        return [cls(*r) for r in reparaciones]

    @classmethod
    def get_by_id(cls, id):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT r.id, r.patente, c.nombre || ' ' || c.apellido AS nombre_apellido, r.fecha_ingreso, r.fecha_egreso, r.descripcion, r.presupuesto, r.estado
            FROM reparaciones r
            JOIN vehiculos v ON r.patente = v.patente
            JOIN clientes c ON v.cliente_id = c.id
            WHERE r.id = ?
        ''', (id,))
        reparacion = cursor.fetchone()
        conn.close()
        return cls(*reparacion) if reparacion else None

    def save(self):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reparaciones (patente, nombre_apellido, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.patente, self.nombre_apellido, self.fecha_ingreso, self.fecha_egreso, self.descripcion, self.presupuesto, self.estado
        ))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE reparaciones
            SET fecha_ingreso = ?, fecha_egreso = ?, descripcion = ?, presupuesto = ?, estado = ?
            WHERE id = ?
        ''', (
            self.fecha_ingreso, self.fecha_egreso, self.descripcion, self.presupuesto, self.estado, self.id
        ))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reparaciones WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()