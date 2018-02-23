from flask import Flask, render_template
import pandas
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/new')
def newfunction():
    conn = psycopg2.connect(database="modcom_db", user="postgres", password="1234", host="localhost", port="5432")
    df = pandas.read_sql_query("SELECT idno FROM emp_details", conn)
    return render_template('start.html', datatorender = df)



@app.route("/wewe")
def help():
    return 'helooooo'

if __name__ == '__main__':
    app.run(debug=True)
