# app.py
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import json
from db import *

app = Flask(__name__)
""" class Reparacion:
    def __init__(self, patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado):
        self.patente = patente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso
        self.descripcion = descripcion
        self.presupuesto = presupuesto
        self.estado = estado

    def save(self, cursor):
        cursor.execute('''
            INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.patente, self.fecha_ingreso, self.fecha_egreso, self.descripcion, self.presupuesto, self.estado))

    @classmethod
    def get_all(cls, cursor):
        cursor.execute('SELECT * FROM reparaciones')
        rows = cursor.fetchall()
        reparaciones = []
        for row in rows:
            reparacion = Reparacion(row[1], row[2], row[3], row[4], row[5], row[6])
            reparacion.id = row[0]
            reparaciones.append(reparacion)
        return reparaciones

    @classmethod
    def get_by_id(cls, id, cursor):
        cursor.execute('SELECT * FROM reparaciones WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            reparacion = Reparacion(row[1], row[2], row[3], row[4], row[5], row[6])
            reparacion.id = row[0]
            return reparacion
        return None

    def update(self, cursor):
        cursor.execute('''
            UPDATE reparaciones SET patente = ?, fecha_ingreso = ?, fecha_egreso = ?, descripcion = ?, presupuesto = ?, estado = ?
            WHERE id = ?
        ''', (self.patente, self.fecha_ingreso, self.fecha_egreso, self.descripcion, self.presupuesto, self.estado, self.id))

    def delete(self, cursor):
        cursor.execute('DELETE FROM reparaciones WHERE id = ?', (self.id,))"""

@app.route('/')
def index():
    reparaciones = show_reparaciones()
    return render_template('index.html', reparaciones=reparaciones)

@app.route('/nueva_reparacion', methods=['POST'])
def nueva_reparacion():
    patente=request.form['patente'],
    fecha_ingreso=request.form['fecha_ingreso'],
    fecha_egreso=request.form['fecha_egreso'],
    descripcion=request.form['descripcion'],
    presupuesto=request.form['presupuesto'],
    estado=request.form['estado']
    insert_reparaciones(patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
    return redirect(url_for('index'))

'''@app.route('/editar_reparacion/<int:id>', methods=['POST'])
def editar_reparacion(id):
    reparacion = Reparacion.get_by_id(id, cursor)
    reparacion.patente = request.form['patente']
    reparacion.fecha_ingreso = request.form['fecha_ingreso']
    reparacion.fecha_egreso = request.form['fecha_egreso']
    reparacion.descripcion = request.form['descripcion']
    reparacion.presupuesto = request.form['presupuesto']
    reparacion.estado = request.form['estado']
    return redirect(url_for('index'))'''

'''@app.route('/eliminar_reparacion/<int:id>')
def eliminar_reparacion(id):
    conn = sqlite3.connect('taller_motos.db')
    cursor = conn.cursor()
    reparacion = Reparacion.get_by_id(id, cursor)
    reparacion.delete(cursor)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))'''

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    