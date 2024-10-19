from app import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def create(email, password_hash, first_name, last_name, phone_no, location, country):
        user = User(email=email, password_hash=password_hash,
                    first_name=first_name, last_name=last_name,
                    phone_no=phone_no, location=location, country=country)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
