from flask import Blueprint, render_template, request, session, redirect, url_for
from app.forms import QuestionsForm
from app.models import Questions
bp = Blueprint("route",__name__ )

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/question/<int:id>", methods = ["POST", "GET"])
def question(id):
    form = QuestionsForm()
    #query database for questions
    questions = Questions.query.filter_by(q_id = id).first()

    if request.method == "POST":

        answer = request.form["options"]
        if answer == questions.ans:
           

            return redirect(url_for('route.question',id =(id +1)))
    form.options.choices =[
                            (questions.a,questions.a),
                            (questions.b,questions.b),
                            (questions.c,questions.c),
                            (questions.d,questions.d)
                        ]
    return render_template("questions.html", form = form, questions = questions)