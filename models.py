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
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s) RETURNING id", (self.username, self._password))
        self._id = cur.fetchone()[0]
        conn.commit()
        conn.close()


a = Users("Paweu", "123456")


