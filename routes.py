from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

cursor = db.cursor()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contacto')
def contacto():
  return render_template('contacto.html')

@app.route('/ficha')
def ficha():
  return render_template('ficha.html')

@app.route('/info')
def info():
  return render_template('info.html')

@app.route('/iniciarsesión')
def iniciarsesión():
  return render_template('iniciarsesión.html')

@app.route('/ir-a-tienda')
def ir_a_tienda():
  return render_template('ir-a-tienda.html')

@app.route('/perfilmascota')
def perfilmascota():
  return render_template('perfilmascota.html')

@app.route('/registrarse')
def registrarse():
  return render_template('registrarse.html')

@app.route('/ver-mascotas')
def ver_mascotas():
  return render_template('ver-mascotas.html')


# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)


# Ruta para manejar el envío del formulario
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        contacto = request.form['contacto']

        # Insertar datos en la base de datos
        sql = "INSERT INTO usuarios (nombre, correo, contraseña, contacto) VALUES (%s, %s, %s, %s)"
        val = (nombre, correo, contraseña, contacto)
        cursor.execute(sql, val)
        db.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

