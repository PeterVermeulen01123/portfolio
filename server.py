from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# function to write to text database neede for submit_form route below
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject=data["subject"]
        message=data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as databaseCSV:
        email = data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(databaseCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'could not write to database'
    else:
        return render_template('index.html')



