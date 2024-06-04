from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def solve(a_quotient, b_quotient, c_quotient):
    a = b = c = 0.0

    if not(is_number(a_quotient)) or a_quotient == "" or float(a_quotient) == 0.0:
        return ["Введён некорректный коэффициент a. Попробуйте снова."]
    else:
        a = float(a_quotient)

    if is_number(b_quotient):
        b = float(b_quotient)
    elif b_quotient != "":
        return ["Введён некорректный коэффициент b. Попробуйте снова."]

    if is_number(c_quotient):
        c = float(c_quotient)
    elif c_quotient != "":
        return ["Введён некорректный коэффициент c. Попробуйте снова."]

    discriminant = b ** 2.0 - 4.0 * a * c

    if discriminant > 0.0:
        x1 = (-b - sqrt(discriminant)) / (2.0 * a)
        x2 = (-b + sqrt(discriminant)) / (2.0 * a)
        x1 = (abs(x1) if x1 == -0.0 else x1)
        x2 = (abs(x2) if x2 == -0.0 else x2)
        return [f"x₁ = { x1 };  x₂ = { x2 }.", x1, x2]
    elif discriminant == 0.0:
        x = -b / (2.0 * a)
        x = (abs(x) if x == -0.0 else x)
        return [f"x₁ = x₂ = { x }.", x]
    else:
        return ["Действительных корней нет."]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        a_quotient = request.form.get("a_quotient")
        b_quotient = request.form.get("b_quotient")
        c_quotient = request.form.get("c_quotient")
        result = solve(a_quotient, b_quotient, c_quotient)
        return render_template("index.html", answer=result[0])


if __name__ == "__main__":
    app.run()
