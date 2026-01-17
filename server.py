from flask import Flask, render_template, url_for, request, redirect
import os
import psycopg
app = Flask(__name__)

def get_db_connection():
    return psycopg.connect(os.environ["DATABASE_URL"])

@app.route("/submit_form", methods=["POST"])
def submit_form():
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not email or not message:
        return "Email and message are required.", 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contact_messages (email, subject, message) VALUES (%s, %s, %s)",
                (email, subject, message)
            )
            conn.commit()

    return redirect("/thankyou.html")

def init_db():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contact_messages (
                    id SERIAL PRIMARY KEY,
                    email TEXT NOT NULL,
                    subject TEXT,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

init_db()

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/thankyou.html")
def thank_you():
    return render_template('thankyou.html')


    





