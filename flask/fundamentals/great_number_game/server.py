from flask import Flask, render_template, request, session, redirect
import os
import random

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)

    message = None
    correct_guess = False
    if request.method == 'POST':
        if 'guess' in request.form:
            guess = int(request.form['guess'])
            if guess > session['number']:
                message = 'Too high!'
            elif guess < session['number']:
                message = 'Too low!'
            else:
                correct_guess = True
                message = f'{session["number"]} was the number!'
        elif 'play_again' in request.form:
            session.pop('number')
            return redirect('/')

    return render_template('index.html', message=message, correct_guess=correct_guess)

if __name__ == '__main__':
    app.run(debug=True)
