from app import db
from john import models


user1 = User("Dula","dimka@gmail.com","1234")

db.session.add(user)
db.session.commit()