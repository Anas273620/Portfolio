from flask import Flask, render_template, url_for, request, redirect
import os
app = Flask(__name__)

@app.route("/submit_form", methods=["POST"])
def submit_form():
    return redirect("/thankyou.html")

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/thankyou.html")
def thank_you():
    return render_template('thankyou.html')


    





