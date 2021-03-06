from flask import *
from flask import render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("main.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template("training.html", prof=prof)


@app.route('/list_prof/<list_param>')
def list_prof(list_param):
    with open("prof.txt", encoding="UTF-8") as profs:
        prof = profs.readlines()
    return render_template("list_prof.html", list_param=list_param, profs=prof)


@app.route('/auto_answer', methods=['POST', 'GET'])
@app.route('/answer', methods=['POST', 'GET'])
def answer():
    if request.method == 'GET':
        return render_template("answer.html")
    elif request.method == 'POST':
        return render_template("auto_answer.html", **request.form)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
