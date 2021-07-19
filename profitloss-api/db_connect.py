import psycopg2 as postgres
from psycopg2 import Error



def connect():
	connection = postgres.connect(user = "postgres",password = "115488", host = "localhost", port = "5432", database = "profit-db")
	
	cursor = connection.cursor()
	cursor.execute("SELECT version()")
	
	print(cursor.fetchone())
	
