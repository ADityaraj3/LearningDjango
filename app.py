from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adityaraj@localhost:5432/jobsdata'

db=SQLAlchemy(app)

class jobsTable(db.Model):
  __tablename__='dataOFJobs'
  id=db.Column(db.Integer,primary_key=True)
  companyName=db.Column(db.String(40))
  title=db.Column(db.String(40))
  location=db.Column(db.String(40))
  salary=db.Column(db.String(40))

  def __init__(self,companyName,title,location,salary):
    self.companyName=companyName
    self.title=title
    self.location=location
    self.salary=salary

app.app_context().push()



@app.route('/submit', methods=['POST'])
def submit():
  companyName= request.form['companyName']
  title=request.form['title']
  location=request.form['location']
  salary=request.form['salary']

  job_entry=jobsTable(companyName,title,location, salary)
  db.session.add(job_entry)
  db.session.commit()

  return render_template('success.html', data=companyName)
  

JOBS = [
  {
    'id':1,
    'title':'Python Developer',
    'location':'New York',
    'salary':'$100,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'New York',
    'salary':'$120,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'New York',
    'salary':'$90,000'
  },
  {
    'id' : 4,
    'title' : 'Backend Engineer',
    'location' : 'New York',
    'salary' : '$110,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/jobitem")
def job_item():
  try:
    print("Entering job_item route")
    job_entries = jobsTable.query.all()
    print("Query successful")
    print(f"Number of jobs: {len(job_entries)}")
    return render_template('jobitem.html', jobs=job_entries)
  except Exception as e:
    print(f"An error occurred: {e}")
    return f"An error occurred: {e}"



if __name__ == '__main__':
  app.run(debug=True)