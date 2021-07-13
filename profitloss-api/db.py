import sqlite3


DATABASE_NAME = "trader-profit.db"

def get_db():
	connection = sqlite3.connect(DATABASE_NAME)
	return connection

def create_tables():
    tables = [
        '''create table if not exists trader-profit(
        	id int primary key auto-increment,
        	name text not null,
        	profit int null
        )
        '''
    ]

    db = get_db()
    cursor = db.cursor()

    for table in tables:
        cursor.execute(table)
