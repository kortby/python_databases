from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost:5432/project_tracker'
app.config['SECRET_KEY'] = '\x8d-\x83\x1bD\xa6\xb7wt\xa3\xc3\xef\xbd\xd8\x90\xb5\x8cJ\xba\x04\xd7,\xf8S'

db = SQLAlchemy(app)

class Project(db.Model):
	__tablename__ = 'projects'

	project_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(length=50))

class Task(db.Model):
	__tablename__ = 'tasks'

	task_id = db.Column(db.Integer, primary_key=True)
	project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
	description = db.Column(db.String(length=50))

	project = db.relationship("Project")

@app.route("/")
def show_projects():
	return render_template("index.html", projects=Project.query.all())

@app.route("/project/<project_id>")
def show_tasks(project_id):
	return render_template("project-tasks.html", 
		project=Project.query.filter_by(project_id=project_id).first(),
		tasks=Task.query.filter_by(project_id=project_id).all())

@app.route("/add/project", methods=['POST'])
def add_project():
	#Add project
	return "Project added sucessfully"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
	#Add task
	return "Task added successfully"

app.run(debug=True, host="127.0.0.1", port=3000)