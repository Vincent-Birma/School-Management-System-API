from fastapi import FastAPI, HTTPException
from fastapi_offline import FastAPIOffline
from pydantic import BaseModel
import sqlite3
from database import connect, staff_table, student_table, course_table
from fastapi.middleware.cors import CORSMiddleware

app = FastAPIOffline(title='School Management System', description='API for School Management System developed by Reuben Vincent Birma')
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"], 
	allow_credentials=True, 
	allow_methods=["*"],
	allow_headers=["*"]
)

staff_table()
student_table()
course_table()

class staff_info(BaseModel):
	Full_Name: str
	Staff_Email: str
	Staff_Position: str
	Staff_Department: str

class student_info(BaseModel):
	Reg_No: str
	Full_Name: str
	Student_Email: str
	student_Department: str
	Student_Level: str

class course_details(BaseModel):
	Reg_No: str
	Full_Name: str
	Student_Email: str
	Student_Department: str
	Student_Courses: str

@app.post('/staff_record')
async def staff_record(staff: staff_info):
	staff_details = [
		staff.Full_Name,
		staff.Staff_Email,
		staff.Staff_Position,
		staff.Staff_Department
	]

	try:
		conn = connect()
		conn.execute("INSERT INTO Staff_record(Name,Email,Position,Department) VALUES(?,?,?,?)", staff_details)
		conn.commit()
		conn.close()
		return {"status": "success", "message": "Staff record added successfully"}
	except sqlite3.IntegrityError:
		raise HTTPException(status_code=400, detail="Staff with that email already exists.")

@app.post('/student_record')
async def student_record(student: student_info):
	student_details = [
		student.Reg_No,
		student.Full_Name,
		student.Student_Email,
		student.student_Department,
		student.Student_Level
	]

	try:
		conn = connect()
		conn.execute("INSERT INTO Student_record(Reg_No,Name,Email,Department,Level) VALUES(?,?,?,?,?)", student_details)
		conn.commit()
		conn.close()
		return {"status": "success", "message": "Student record added successfully"}
	except sqlite3.IntegrityError:
		raise HTTPException(status_code=400, detail="Student record already exists for this Reg No.")

@app.post('/course_record')
async def course_record(course: course_details):
	course_detail = [
		course.Reg_No,
		course.Full_Name,
		course.Student_Email,
		course.Student_Department,
		course.Student_Courses
	]

	try:
		conn = connect()
		conn.execute("INSERT INTO Course_registraton(Reg_No,Name,Email,Department,Courses) VALUES(?,?,?,?,?)", course_detail)
		conn.commit()
		conn.close()
		return {"status": "success", "message": "Course registration record added successfully"}
	except sqlite3.IntegrityError:
		raise HTTPException(status_code=400, detail="Course registration already exists for this Reg No.")

@app.get('/staff_data')
async def staff_data():
	conn = connect()
	rows = conn.execute("SELECT * FROM Staff_record").fetchall()
	conn.close()
	return [dict(row) for row in rows]

@app.get('/student_data')
async def student_data():
	conn = connect()
	rows = conn.execute("SELECT * FROM Student_record").fetchall()
	conn.close()
	return [dict(row) for row in rows]

@app.get('/course_reg')
async def course_registration():
	conn = connect()
	rows = conn.execute("SELECT * FROM Course_registraton").fetchall()
	conn.close()
	return [dict(row) for row in rows]