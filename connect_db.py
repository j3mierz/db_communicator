from psycopg2 import connect

settings = {
    'database': 'communicator',
    'user': 'postgres',
    'host': '127.0.0.1',
    'port': '5432',
    'password': 'coderslab',
}


def connect_db():
    return connect(**settings)
