from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# Wait until MySQL is ready
db = None
while db is None:
    try:
        db = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="root123",
            database="notesdb"
        )
    except:
        print("Waiting for MySQL...")
        time.sleep(3)

cursor = db.cursor()


@app.route("/")
def index():
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    note = request.form["note"]

    if note.strip() != "":
        sql = "INSERT INTO notes(note) VALUES(%s)"
        cursor.execute(sql, (note,))
        db.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_note(id):
    sql = "DELETE FROM notes WHERE id=%s"
    cursor.execute(sql, (id,))
    db.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
