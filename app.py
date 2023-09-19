from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calc.db'
db = SQLAlchemy(app)

class Calculator_History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(200), nullable=False)
    output_value = db.Column(db.Float(200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
@app.get("/")
def hist():
    hist_list = []
    hist = Calculator_History.query.order_by(Calculator_History.date_created).all()

    for h in hist:
        hist_list.append(Calculator_History.as_dict(h))
    
    return hist_list

@app.post("/")
def index():
    usr_input = request.get_json()['user_input']
    opt_value = request.get_json()['output_value']

    new_hist = Calculator_History(user_input = usr_input,output_value=opt_value)
    db.session.add(new_hist)
    db.session.commit()
    hist_list = []
    hist = Calculator_History.query.order_by(Calculator_History.date_created).all()

    for h in hist:
        hist_list.append(Calculator_History.as_dict(h))
    
    return hist_list

@app.delete("/clear")
def clear():
    hist = Calculator_History.query.all()
    for h in hist:
        db.session.delete(h)
    db.session.commit()
    return "all clear"