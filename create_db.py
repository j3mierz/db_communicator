import psycopg2
from psycopg2 import connect

settings = {
    'database': 'postgres',
    'user': 'postgres',
    'host': '127.0.0.1',
    'port': '5432',
    'password': 'coderslab',
}

connection = psycopg2.connect(**settings)
cnn = connection.close()