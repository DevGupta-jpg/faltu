from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flask_practice"
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO contacts (name, email, message)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, message))

    connection.commit()

    cursor.close()
    connection.close()

    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True)