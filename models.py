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

    def load_user_by_username(self, username):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"select * from users where username like '{username}'")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result


a = Users()
print(a.load_user_by_username('Paweu'))