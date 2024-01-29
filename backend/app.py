from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_CONNECTION")
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/*": {"origins": "http://sila-frontend:3000"}})

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        tasks_list = [{'id': task.id, 'title': task.title} for task in tasks]
        return jsonify(tasks_list)
    elif request.method == 'POST':
        data = request.get_json()
        new_task = Task(title=data['title'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'GET':
        return jsonify({'id': task.id, 'title': task.title})
    elif request.method == 'PUT':
        data = request.get_json()
        task.title = data['title']
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)