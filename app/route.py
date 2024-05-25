from flask import Blueprint, render_template
from app.forms import QuestionsForm
from app.models import User
bp = Blueprint("route",__name__ )

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/question/<int:id>", methods = ["POST", "GET"])
def question(id):
    form = QuestionsForm()
    #query database for questions
    questions = User.query.filter_by(q_id = id)
    form.options.choices =[
                            (question.a,question.a,),
                            (question.b,question.b),
                            (question.c,question.c),
                            (question.d,question.d)
                        ]
    return render_template("questions.html", form = form)