from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)

class Details(db.Model):
	__tablename__ = 'details'
	id = db.Column(db.Integer, primary_key=True)
	studentid = db.Column(db.Integer, nullable=False)
	firstname = db.Column(db.String(64), nullable=False)
	lastname = db.Column(db.String(64), nullable=False)
	dob = db.Column(db.String(64), nullable=False)
	amountdue = db.Column(db.Integer, nullable=False)
	
	def json(self):
		return {'id': self.id, 'studentid': self.studentid, 'firstname': self.firstname, 'lastname': self.lastname, 'dob': self.dob, 'amountdue': self.amountdue}
	
	def add_student(_studentid, _firstname, _lastname, _dob, _amountdue):
		new_student = Details(studentid = _studentid, firstname = _firstname, lastname = _lastname, dob = _dob, amountdue = _amountdue)
		db.session.add(new_student)  
		db.session.commit()  
		
	def get_all_students():
		return [Details.json(student) for student in Details.query.all()]
		
	def get_student(_id):
		return [Details.json(Details.query.filter_by(id=_id).first())]
		
	def update_student(_id, _studentid, _firstname, _lastname, _dob, _amountdue):
		student_to_update = Details.query.filter_by(id=_id).first()
		student_to_update.studentid = _studentid
		student_to_update.firstname = _firstname
		student_to_update.lastname = _lastname
		student_to_update.dob = _dob
		student_to_update.amountdue = _amountdue
		db.session.commit()
		
	def delete_student(_id):
		Details.query.filter_by(id=_id).delete()
		db.session.commit()
	
				