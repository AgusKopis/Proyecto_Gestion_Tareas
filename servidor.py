from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import sqlite3
from flask import render_template_string

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Crear base y tabla si no existen
def init_db():
    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    contraseña_hashed = bcrypt.generate_password_hash(contraseña).decode('utf-8')

    try:
        conn = sqlite3.connect('base_datos.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña_hashed))
        conn.commit()
        conn.close()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and bcrypt.check_password_hash(resultado[0], contraseña):
        return jsonify({'mensaje': f'Bienvenida, {usuario}!'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401
    
@app.route('/tareas', methods=['GET'])
def ver_tareas():
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenida</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; }
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <h1>¡Bienvenida al Gestor de Tareas, {{usuario}}!</h1>
        <p>Aquí próximamente verás tus tareas 😉</p>
    </body>
    </html>
    """
    # Por ahora es un mensaje genérico, más adelante podríamos pasarlo como variable si está logueada
    return render_template_string(html_bienvenida, usuario="Agustina")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
