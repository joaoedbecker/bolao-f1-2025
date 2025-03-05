from flask_login import UserMixin
import sqlite3

class Usuario(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def buscar_usuario(username):
        conn = sqlite3.connect('bolao.db')
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            return Usuario(*user_data)
        return None

    @staticmethod
    def buscar_usuario_por_id(user_id):
        conn = sqlite3.connect('bolao.db')
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            return Usuario(*user_data)
        return None
