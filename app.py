# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_mail import Mail, Message
from db import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # La direccion de correo desde donde se envia los mail de recuperacion
app.config['MAIL_PASSWORD'] = 'tu_contraseña'        # Tu contraseña del correo (Usar contraseñas de aplicaciones en Gmail)
app.config['MAIL_DEFAULT_SENDER'] = ('Nombre Empresa', 'tu_correo@gmail.com')

mail = Mail(app)

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

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contraseña = request.form['contraseña']
        # Aquí hasheas la contraseña y la insertas en la base de datos
        contraseña_hasheada = generate_password_hash(contraseña)
        registrar_usuario(nombre_usuario, contraseña_hasheada)
        flash('Usuario registrado exitosamente, ahora puedes iniciar sesión')
        return redirect(url_for('login'))
    
    return render_template('registrar.html')

@app.route('/enviar_correo')
def enviar_correo():
    try:
        msg = Message('Recuperar tu contraseña', 
                    recipients=['usuario@correo.com'])  # Destinatarios
        msg.body = 'Haz clic en el enlace para restablecer tu contraseña.'
        msg.html = '<b>Haz clic aquí</b> para <a href="http://tusitio.com/resetear_contraseña">restablecer tu contraseña</a>.' # CAMBIAR LA DIRECCION URL
        
        mail.send(msg)
        return "Correo enviado exitosamente."
    except Exception as e:
        return f"Error enviando correo: {e}"

@app.route('/olvidar_contraseña', methods=['GET', 'POST'])
def olvidar_contraseña():
    if request.method == 'POST':
        correo = request.form['correo']
        
        # Conexión a la base de datos y verificación de usuario
        conexion = mysql.connector.connect(user='root', password='tu_password', database='tu_db')
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo_electronico = %s", (correo,))
        usuario = cursor.fetchone()
        
        if usuario:
            # Crear y enviar el correo
            token_recuperacion = 'enlace_unico_generado'  # Generar un token único para el usuario
            enlace_recuperacion = url_for('resetear_contraseña', token=token_recuperacion, _external=True)
            
            msg = Message('Recuperación de contraseña',
                        recipients=[correo])
            msg.body = f'Haz clic en el siguiente enlace para recuperar tu contraseña: {enlace_recuperacion}'
            msg.html = f'<p>Haz clic en el siguiente enlace para recuperar tu contraseña:</p> <a href="{enlace_recuperacion}">Recuperar Contraseña</a>'
            
            mail.send(msg)
            flash('Se ha enviado un enlace de recuperación a tu correo electrónico.')
            return redirect(url_for('login'))
        else:
            flash('El correo no está registrado.')
    
    return render_template('olvidar_contraseña.html') # EDITAR CON LOS NOMBRES DE LOS ARCHIVOS CORRESPONDIENTES


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    