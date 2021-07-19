import psycopg2 as postgres
from psycopg2 import Error


class database:

	@staticmethod
	def connect():
		connection = postgres.connect(user = "postgres",password = "115488", host = "localhost", port = "5432", database = "profit-db")
		cursor = connection.cursor()

		return cursor
