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



    <!-- Main Content -->
    <div class="container">
        <div class="jumbotron text-center animate__animated animate__fadeIn">
            <h1 class="display-4">Welcome to the Quiz App!</h1>
            <p class="lead">Test your knowledge with our exciting quizzes.<br
                
                Answer multiple-choice questions and see how well you score!</p>
            <hr class="my-4">
            <p>Ready to start? Click the button below to begin the quiz.</p>
            <a class="btn btn-primary btn-lg start-btn animate__animated animate__bounceIn" href="{{ url_for('auth.login') }}" role="button">Start Quiz</a>
        </div>
        <div class="row">
            <div class="col-md-4">
                <img src="https://via.placeholder.com/300" class="img-fluid rounded quiz-image animate__animated animate__zoomIn" alt="Quiz Image 1">
                <h3 class="text-center">Quiz 1</h3>
                <p class="text-center">Challenge yourself with a variety of topics.</p>
            </div>
            <div class="col-md-4">
                <img src="https://via.placeholder.com/300" class="img-fluid rounded quiz-image animate__animated animate__zoomIn animate__delay-1s" alt="Quiz Image 2">
                <h3 class="text-center">Quiz 2</h3>
                <p class="text-center">Test your knowledge and improve your skills.</p>
            </div>
            <div class="col-md-4">
                <img src="https://via.placeholder.com/300" class="img-fluid rounded quiz-image animate__animated animate__zoomIn animate__delay-2s" alt="Quiz Image 3">
                <h3 class="text-center">Quiz 3</h3>
                <p class="text-center">Learn new facts and have fun.</p>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer text-center mt-5">
        <div class="container">
            <p class="mb-0">© 2024 Quiz App. All rights reserved.</p>
            <div class="mt-2">
                <a href="#" class="text-decoration-none">Privacy Policy</a>
                <a href="#" class="text-decoration-none">Terms of Service</a>
                <a href="#" class="text-decoration-none">Contact Us</a>
            </div>
        </div>
    </footer>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


base 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title if title else "Quiz App" }}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />

</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        {% if current_user.is_authenticated %}
        <a class="navbar-brand" href="{{ url_for('auth.profile') }}">Profile</a>
        {% else %}
        <a class="navbar-brand" href="{{ url_for('route.index') }}">Quiz App</a>
        {% endif %}
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                {% if current_user.is_authenticated %}
                <li class="nav-item">
                    <a class="nav-link" href="{{ url_for('auth.logout') }}">Logout</a>
                </li>
                {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('auth.login') }}">Login</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('auth.register') }}">Register</a>
                    </li>

                    {% endif %}
            </ul>
        </div>


<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>