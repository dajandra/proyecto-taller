# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import json

app = Flask(__name__)

# Conexión a la base de datos
conn = sqlite3.connect('taller_motos.db')
cursor = conn.cursor()

class Reparacion:
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
        cursor.execute('DELETE FROM reparaciones WHERE id = ?', (self.id,))

@app.route('/')
def index():
    conn = sqlite3.connect('taller_motos.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT r.id, r.patente, r.fecha_ingreso, r.fecha_egreso, r.descripcion, r.presupuesto, r.estado, c.nombre_apellido
    FROM reparaciones r
    JOIN vehiculos v ON r.patente = v.patente
    JOIN clientes c ON v.patente = c.vehiculo_patente;
''')
    reparaciones = cursor.fetchall()
    conn.close()
    reparaciones = [
        {'id': r[0], 'patente': r[1], 'fecha_ingreso': r[2], 'fecha_egreso': r[3], 'descripcion': r[4], 'presupuesto': r[5], 'estado': r[6], 'nombre_apellido': r[7]}
        for r in reparaciones
    ]
    return render_template('index.html', reparaciones=reparaciones)


@app.route('/editar_reparacion/<int:id>', methods=['POST'])
def editar_reparacion(id):
    conn = sqlite3.connect('taller_motos.db')
    cursor = conn.cursor()
    reparacion = Reparacion.get_by_id(id, cursor)
    reparacion.patente = request.form['patente']
    reparacion.fecha_ingreso = request.form['fecha_ingreso']
    reparacion.fecha_egreso = request.form['fecha_egreso']
    reparacion.descripcion = request.form['descripcion']
    reparacion.presupuesto = request.form['presupuesto']
    reparacion.estado = request.form['estado']
    reparacion.update(cursor)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/eliminar_reparacion/<int:id>')
def eliminar_reparacion(id):
    conn = sqlite3.connect('taller_motos.db')
    cursor = conn.cursor()
    reparacion = Reparacion.get_by_id(id, cursor)
    reparacion.delete(cursor)
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/reparaciones/estado', methods=['GET'])
def get_reparaciones_por_estado():
    estado = request.args.get('estado')
    reparaciones = Reparacion.query.filter_by(estado=estado).all()
    data = [reparacion.to_dict() for reparacion in reparaciones]
    return json.dumps(data), 200, {'Content-Type': 'application/json'}

@app.route('/nueva_reparacion', methods=['GET', 'POST'])
def nueva_reparacion():
    if request.method == 'POST':
        patente = request.form['patente']
        fecha_ingreso = request.form['fecha_ingreso']
        fecha_egreso = request.form['fecha_egreso']
        descripcion = request.form['descripcion']
        presupuesto = request.form['presupuesto']
        estado = request.form['estado']
        
        # Crear una nueva reparación en la base de datos
        conn = sqlite3.connect('taller_motos.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reparaciones (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (patente, fecha_ingreso, fecha_egreso, descripcion, presupuesto, estado))
        conn.commit()
        conn.close()
        
        # Redirigir a la página principal
        return redirect(url_for('index'))
    return render_template('nueva_reparacion.html')