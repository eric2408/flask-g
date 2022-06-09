# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def showAdd():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = add(a,b)

    return str(answer)

@app.route('/sub')
def showSub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = sub(a,b)

    return str(answer)

@app.route('/mult')
def showMult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = mult(a,b)

    return str(answer)

@app.route('/div')
def showDiv():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = div(a,b)

    return str(answer)




operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)