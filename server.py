from flask import Flask, render_template, url_for, request, redirect
import csv
import os
import psycopg
app = Flask(__name__)

def get_db_connection():
    return psycopg.connect(os.environ["DATABASE_URL"])

@app.route("/submit_form", methods=["POST"])
def submit_form():
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contact_messages (email, subject, message) VALUES (%s, %s, %s)",
                (email, subject, message)
            )
            conn.commit()

    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/thankyou.html")
def thank_you():
    return render_template('thankyou.html')


    





