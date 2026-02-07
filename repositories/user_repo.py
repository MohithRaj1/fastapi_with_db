from models import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: session):
       self.db = db

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
    
        return user

   