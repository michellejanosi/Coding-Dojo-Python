from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your secret key'  # for practice assignment, leaving this as is.

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['data'] = request.form
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html", result=session['data'])

if __name__ == '__main__':
    app.run(debug=True)
