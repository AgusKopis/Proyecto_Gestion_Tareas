# 🗂️ Sistema de Gestión de Tareas - PFO 2

Proyecto práctico para la materia Programación de Frontend y Backend, desarrollado en Flask + SQLite con autenticación segura y persistencia de datos.

---

## 🚀 Funcionalidades

- Registro de usuarios con contraseñas hasheadas
- Inicio de sesión con verificación de credenciales
- Gestión de tareas: creación y visualización
- Cliente de consola (`cliente.py`) para interacción sin interfaz web
- Base de datos persistente con SQLite
- Capturas de prueba en carpeta `/capturas/`
- Sitio informativo en GitHub Pages

---

## 🧩 Estructura del proyecto

gestor_tareas_api/ 
├── servidor.py 
├── cliente.py 
├── base_datos.db 
├── requirements.txt 
├── README.md 
├── index.html 
└── capturas/


---

## ⚙️ Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/AgusKopis/Proyecto_Gestion_De_Tareas.git
cd Proyecto_Gestor_De_Tareas

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor
python servidor.py

🔐 Endpoints disponibles
Método	Ruta	              Descripción
POST	/registro	            Registro de usuario
POST	/login	              Inicio de sesión
POST	/tareas	              Crear tarea
GET	/tareas?usuario=nombre	Ver tareas del usuario

💻 Cliente de consola (cliente.py)
Permite registrar, loguear, crear tareas y visualizarlas sin Postman ni navegador.

python cliente.py


📷 Capturas de prueba

Las capturas están en la carpeta capturas/, incluyendo:

Registro exitoso
Login exitoso y fallido
Creación de tarea
Listado de tareas
Menú en cliente por consola

🌐 Enlaces
Repositorio: https://github.com/AgusKopis/Proyecto_Gestio_de_Tareas

GitHub Pages: https://AgusKopis.github.io/Proyecto_Gestion_De_Tareas/