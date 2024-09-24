# models.py
import sqlite3

class Reparacion:
    def __init__(self, patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado):
        self.patente = patente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso
        self.descripcion = descripcion
        self.presupuesto = presupuesto
        self.estado = estado

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reparaciones')
        reparaciones = cursor.fetchall()
        conn.close()
        return [cls(*r[1:]) for r in reparaciones]

    @classmethod
    def get_by_id(cls, id):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reparaciones WHERE id = ?', (id,))
        reparacion = cursor.fetchone()
        conn.close()
        return cls(*reparacion[1:]) if reparacion else None

    def save(self):
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            self.patente, self.fecha_ingreso, self.fecha_egreso, self.descripcion, self.presupuesto, self.estado
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