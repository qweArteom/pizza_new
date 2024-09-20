from flask import Flask, render_template, request, redirect

from app.data import db


app = Flask(__name__, static_folder="app/static", template_folder="app/templates")


@app.get("/")
def index():
    return render_template("index.html", title="Test DB")


@app.get("/students/")
def students():
    students_data = db.get_students().get("students")

    context = {
        "title": "List of students",
        "students": students_data
    }
    return render_template("students.html", **context)


@app.get("/add_student/")
def add_student():
    return render_template("add_student.html", title="Add student")


@app.post("/add_student/")
def save_student():
    data = request.form

    print(f"{data = }")

    db.insert_data_by_values(**data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
