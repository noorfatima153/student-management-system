from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "student_management_secret"

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Noor457495",
    "database": "student_management"
}

def get_connection():
    return mysql.connector.connect(**db_config)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
        admin = cur.fetchone()
        conn.close()

        if admin:
            session["admin"] = username
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()

    return render_template("dashboard.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if "admin" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        student_id = request.form["student_id"]
        name = request.form["name"]
        age = request.form["age"]
        department = request.form["department"]
        email = request.form["email"]
        cgpa = request.form["cgpa"]

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO students(student_id,name,age,department,email,cgpa)
        VALUES(%s,%s,%s,%s,%s,%s)
        """, (student_id,name,age,department,email,cgpa))
        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("add_student.html")

@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        department = request.form["department"]
        email = request.form["email"]
        cgpa = request.form["cgpa"]

        cur.execute("""
        UPDATE students
        SET name=%s, age=%s, department=%s, email=%s, cgpa=%s
        WHERE id=%s
        """, (name, age, department, email, cgpa, id))

        conn.commit()
        conn.close()
        return redirect(url_for("dashboard"))

    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()
    conn.close()

    return render_template("update_student.html", student=student)

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form["keyword"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM students
    WHERE name LIKE %s OR department LIKE %s OR student_id LIKE %s
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

    students = cur.fetchall()
    conn.close()

    return render_template("dashboard.html", students=students)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
