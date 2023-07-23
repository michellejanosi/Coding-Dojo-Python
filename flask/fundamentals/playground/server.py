from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=3, color='skyblue')

@app.route('/play/<int:x>')
def play_x(x):
    return render_template("index.html", times=x, color='skyblue')

@app.route('/play/<int:x>/<string:color>')
def play_x_color(x, color):
    return render_template("index.html", times=x, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__=="__main__":
    app.run(debug=True)
