from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import sqlite3
from flask import render_template_string

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Crear base y tabla si no existe
def init_db():
    with sqlite3.connect("base_datos.db") as conn:
        cursor = conn.cursor()
        # Tabla de usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            )
        """)
        # Tabla de tareas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                estado TEXT DEFAULT 'pendiente',
                FOREIGN KEY(usuario) REFERENCES usuarios(usuario)
            )
        """)
        conn.commit()
        
# Endpoint de registro
@app.route('/registro', methods=['POST'])
def registrar():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    contraseña_hashed = bcrypt.generate_password_hash(contraseña).decode('utf-8')

    try:
        with sqlite3.connect("base_datos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña_hashed))
            conn.commit()
        return jsonify({"mensaje": f"Usuario '{usuario}' registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409

# Endpoint de login  
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    with sqlite3.connect("base_datos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

    if resultado and bcrypt.check_password_hash(resultado[0], contraseña):
        return jsonify({"mensaje": f"Bienvenida, {usuario}"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Endpoint obtener tareas
@app.route("/tareas", methods=["GET"])
def listar_tareas():
    usuario = request.args.get("usuario")

    if not usuario:
        return jsonify({"error": "Falta el usuario en los parámetros"}), 400

    with sqlite3.connect("base_datos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, descripcion, estado FROM tareas WHERE usuario = ?", (usuario,))
        tareas = cursor.fetchall()

    lista = [{"id": t[0], "descripcion": t[1], "estado": t[2]} for t in tareas]
    return jsonify(lista)

# Endpoint para agregar tareas
@app.route("/tareas", methods=["POST"])
def crear_tarea():
    data = request.get_json()
    usuario = data.get("usuario")
    descripcion = data.get("descripcion")

    if not usuario or not descripcion:
        return jsonify({"error": "Faltan datos"}), 400

    with sqlite3.connect("base_datos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tareas (usuario, descripcion) VALUES (?, ?)", (usuario, descripcion))
        conn.commit()

    return jsonify({"mensaje": f"Tarea agregada para {usuario}"}), 201
    
# Ejecutar el servidor
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
