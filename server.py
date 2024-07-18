from flask import Flask, render_template, url_for, request, redirect
import re
app = Flask(__name__)
import csv

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods =['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something wrong while submitting this form'

def write_file(data):
    with open('database.txt', 'a') as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f'\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n') 

def write_csv(data):
    with open('database.csv', 'a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database)
        csv_file.writerow([email,subject,message])