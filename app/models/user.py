from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)  
    last_name = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(15), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'
