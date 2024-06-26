from connect_db import connect_db


class Users:
    def __init__(self, name="", password=""):
        self._id = -1
        self.username = name
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def password(self):
        return self._password

    def new_user_to_db(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s) RETURNING id",
                    (self.username, self._password))
        self._id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def load_user_by_username(username):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE username LIKE '{username}'")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def change_user(username, password):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"UPDATE users SET username = '{username}', password = '{password}' WHERE username like '{username}'; ")
        conn.commit()
        cur.close()
        conn.close()



    @staticmethod
    def load_user_by_id(user_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {int(user_id)}")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def load_all_users():
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def delete_user_by_id(user_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE id = {int(user_id)};")
        conn.commit()
        cur.close()
        conn.close()


class Messages:
    def __init__(self, from_id="", to_id="", text=""):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_time = None

    @property
    def id(self):
        return self._id

    def save_to_db(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO messages(from_id, to_id, text) VALUES ('{self.from_id}', '{self.to_id}', '{self.text}') RETURNING id")
        self._id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def load_all_messages(id_us):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM messages where to_id = {id_us}")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result


