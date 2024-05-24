from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for CSRF protection
class QuestionForm(FlaskForm):
    options = RadioField('Options what is your name: ', validators=[DataRequired()], default=1)
    submit = SubmitField('Next')
@app.route('/', methods=['GET', 'POST'])
def question():
    form = QuestionForm()
    # Example options for the radio field
    form.options.choices = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4')
    ]
    
    if form.validate_on_submit():
        selected_option = form
        # Handle the selected option (e.g., save to the database, update score)
        return redirect(url_for('next_question'))  # Redirect to the next question or result page

    return render_template('index.html', form=form)

@app.route('/next_question', methods = ["POST", "GET"])
def next_question():
    form = QuestionForm()
    # Example options for the radio field
    form.options.choices = [
        ('3', 'Option 4'),
        ('2', 'Option 2'),
        ('3', 'Option 45'),
        ('4', 'Option 460')
    ]
 
    return  render_template("index.html", form = form)


if __name__=='__main__':
    app.run()
