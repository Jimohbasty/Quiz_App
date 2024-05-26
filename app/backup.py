@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/question/<int:id>", methods = ["POST", "GET"])
def question(id):
    form = QuestionsForm()
    #query database for questions
    questions = Questions.query.filter_by(q_id = id).first()
    if 'score' not in session:
        session['score'] = 0
    if questions is None:
        return str(session['score'])

    if request.method == "POST":

        answer = request.form["options"]
        if answer == questions.ans:
           session['score'] += 1
        return redirect(url_for('route.question',id =(id +1)))
    form.options.choices =[
                            (questions.a,questions.a),
                            (questions.b,questions.b),
                            (questions.c,questions.c),
                            (questions.d,questions.d)
                        ]
    return render_template("questions.html", form = form, questions = questions)



{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <div class="card">
        <div class="card-header">
            <h2>Questions {{ questions.q_id }}</h2>
        </div>
        <div class="card-body">
            <form method="POST" novalidate>
                {{ form.hidden_tag() }}
                <h4 class="card-title">{{ questions.ques }}</h4>
                <div class="form-group mt-3">
                    {% for option in form.options %}
                        <div class="form-check">
                            {{ option(class="form-check-input") }}
                            <label class="form-check-label">{{ option.label.text }}</label>
                        </div>
                    {% endfor %}
                </div>
                <div class="form-group mt-4">
                    {{ form.submit(class="btn btn-primary btn-lg") }}
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}