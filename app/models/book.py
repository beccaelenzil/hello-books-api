from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
<<<<<<< HEAD
    author = db.Column(db.String)
=======
    isbn = db.Column(db.Integer)
>>>>>>> 5005333f52d569c71a4e019405b52e2537f0f9f1
