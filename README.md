# 🗂️ Sistema de Gestión de Tareas (Flask + SQLite)

## ⚙️ Cómo ejecutar el proyecto

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repo.git
   cd tu_repo

2. Instalá las dependencias:
    pip install -r requirements.txt

3. Ejecutá el servidor:
    python servidor.py

# ✨ Endpoints disponibles

POST /registro

Registra un nuevo usuario. Body:

{
  "usuario": "Agustina",
  "contraseña": "1234"
}

POST /login

Verifica el usuario y contraseña. Body: igual al registro.

