from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres1234@localhost:5432/jobsdata'

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


# with app.app_context():
#   db.create_all()

# app.route('/submit', methods=['POST'])
# def submit():
#   fname= request.form['fname']
#   lname=request.form['lname']
#   pet=request.form['pets']

#   student=Student(fname,lname,pet)
#   db.session.add(student)
#   db.session.commit()

#   #fetch a certain student2
#   studentResult=db.session.query(Student).filter(Student.id==1)
#   for result in studentResult:
#     print(result.fname)

#   return render_template('success.html', data=fname)

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

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
