import sqlite3

def connect():
	def db_connect():
	conn = sqlite3.connect('School.db')
	conn.row_factory = sqlite3.Row
	return conn

def staff_table():
	conn = connect()
	conn.execute(""" 
			CREATE TABLE IF NOT EXITS Staff_record
			 (
			 	Id INTEGER PRIMARY KEY AUTOINCREMENT,
			 	Name TEXT NOT NULL,
			 	Email VARCHAR NOT NULL UNIQUE,
			 	Position VARCHAR NOT NULL,
			 	Department TEXT NOT NULL
				)
		""")
	conn.commit()
	conn.close()

def student_table():
	conn = connect()
	conn.execute(""" CREATE TABLE IF NOT EXITS Student_record
		(
				Id INTEGER PRIMARY KEY AUTOINCREMENT,
				Reg_No VARCHAR NOT NULL UNIQUE,
			 	Name TEXT NOT NULL,
			 	Email VARCHAR NOT NULL UNIQUE,
			 	Department TEXT NOT NULL,
			 	Level VARCHAR NOT NULL
		)
		 """)
	conn.commit()
	conn.close()

def course_table():
	conn = connect()
	conn.execute(""" CREATE TABLE IF NOT EXITS Course_registraton
		(
				Id INTEGER PRIMARY KEY AUTOINCREMENT,
				Reg_No VARCHAR NOT NULL UNIQUE,
			 	Name TEXT NOT NULL,
			 	Email VARCHAR NOT NULL UNIQUE,
			 	Department TEXT NOT NULL,
			 	Courses VARCHAR NOT NULL
		)
		 """)
	conn.commit()
	conn.close()