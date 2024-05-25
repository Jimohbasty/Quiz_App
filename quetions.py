from app import create_app, db
from app.models import Questions
app = create_app()

with app.app_context():
    q1 = Questions(
        ques = "Which among the following is not a Laptop?",
        a = "HP",
        b = "Dell",
        c = "Tesla",
        d = "Toshiba",
        ans ="Tesla" 
    )
    db.session.add(q1)
    db.session.commit()