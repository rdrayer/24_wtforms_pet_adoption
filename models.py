from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<pet id={p.id} name={p.name} species={p.species} age={p.age}"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True) 
    name = db.Column(db.String,
                     nullable=False)  
    species = db.Column(db.String,
                        nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean,
                          default=True)