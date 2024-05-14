import psycopg2
from psycopg2 import connect

settings = {
    'database': 'postgres',
    'user': 'postgres',
    'host': '127.0.0.1',
    'port': '5432',
    'password': 'coderslab',
}

create_db = 'CREATE DATABASE Communicator;'

create_table = """CREATE TABLE  users (
    id serial primary key,
    username varchar(255),
    password varchar(80)
);"""
create_table_2 = """CREATE TABLE  messages (
    id serial primary key,
    from_id int,
    to_id int,
    creation_date timestamp,
    text varchar(255)
);"""
try:
    connection = connect(**settings)
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(create_db)
        print('Database created')
    except psycopg2.DatabaseError as e:
        print('database already exist', e)


    cursor.close()
    connection.close()
except psycopg2.Error as e:
    print("connetion Error: ", e)

settings['database'] = 'communicator'
try:
    connection = connect(**settings)
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(create_table)
        print('table created')
    except psycopg2.DatabaseError as e:
        print('table already exists', e)
    try:
        cursor.execute(create_table_2)
        print('table_2 created')
    except psycopg2.DatabaseError as e:
        print('table_2 already exists', e)
    cursor.close()
    connection.close()
except psycopg2.Error as e:
    print("connetion Error: ", e)
