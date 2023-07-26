from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    if 'counter' not in session:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['counter'] += 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 1
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form.get('increment_value'))
    session['counter'] += increment_value
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
