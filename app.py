from details import db
db.create_all()

from details import *

# route to get all students
@app.route('/', methods=['GET'])
def get_home():
	return jsonify({'Students':'This is Home Page'})

# route to get all students
@app.route('/students', methods=['GET'])
def get_students():
	return jsonify({'Students': Details.get_all_students()})
	
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
	print(id);
	return_value = Details.get_student(id)
	return jsonify(return_value)
	
@app.route('/students', methods=['POST'])
def add_student():
	'''Function to add new student to our database'''
	request_data = request.get_json()
	print(request_data);
	Details.add_student(request_data["studentid"], request_data["firstname"],
						request_data["lastname"], request_data["dob"],
						request_data["amountdue"])
	response = Response("Student added", 201, mimetype='application/json')
	return response
	
# route to update student with PUT method
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
	'''Function to edit student in our database using student id'''
	request_data = request.get_json()
	Details.update_student(id, request_data["studentid"], request_data["firstname"],
						request_data["lastname"], request_data["dob"],
						request_data["amountdue"])
	response = Response("Srudent details Updated", status=200, mimetype='application/json')
	return response


@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    '''Function to delete student from our database'''
    Details.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
	app.run(debug=True)