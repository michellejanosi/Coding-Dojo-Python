from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', x=8, y=8, color1='black', color2='red')

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_template('index.html', x=x, y=8, color1='black', color2='red')

@app.route('/<int:x>/<int:y>')
def checkerboard_xy(x, y):
    return render_template('index.html', x=x, y=y, color1='black', color2='red')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_xy_color(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
