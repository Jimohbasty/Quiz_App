from app import create_app, db
from app.models import Questions
app = create_app()

with app.app_context():
    # q1 = Questions(
    #     ques = "Which among the following is not a Laptop?",
    #     a = "HP",
    #     b = "Dell",
    #     c = "Tesla",
    #     d = "Toshiba",
    #     ans ="Tesla" 
    # )
    q2 = Questions(
        ques = "Which among following are example of Odumeje powers except?",
        a = "Abido Shaker",
        b = "Gandusa Ganduja",
        c = "Indaboski Bahose",
        d = "Kadosh Kadosh",
        ans ="Kadosh Kadosh" 
    )
    # db.session.add(q1)
    db.session.add(q2)
    db.session.commit()