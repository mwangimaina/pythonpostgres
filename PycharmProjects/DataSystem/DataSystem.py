from flask import Flask,render_template,Response,request
import psycopg2
import pandas
import pygal
import seaborn
import matplotlib.pyplot as plt
import io

import dateutil
import base64
from dateutil.relativedelta import *
from pygal.style import Style

app = Flask(__name__)
# global connection
conn = psycopg2.connect(database="modcom_db",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")

# lets create a template for this route
@app.route('/')
def hello_world():
    return render_template('home.html')
    # we return our template

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/save", methods=['POST','GET'])
def save():
    if request.method=='POST':
        # create a cursor object, to execute queries
        cursor = conn.cursor()
        sql = "INSERT INTO emp_details VALUES(%s,%s,%s,%s,%s,%s)"
        # prepare data to save
        idno = request.form['idno']
        dob = request.form['dob']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        date_joined = request.form['date_joined']
        cursor.execute(sql,
                       (idno,dob,fname,lname,gender,date_joined))
        conn.commit()
        return render_template('save.html',msg="Saved")
    else:
       return render_template('save.html')



@app.route("/search", methods=['POST','GET'])
def search():
    if request.method=='POST':
        gender = request.form['gender']
        gender = gender.upper()
        dataframe = pandas.read_sql_query("SELECT * FROM emp_details WHERE gender=%s LIMIT 60",conn,params=[gender])
        print(dataframe)
        list = []
        # for x in dataframe['dob'].tolist():
        #      y= x.split("-")
        #      list.append(int(y[0]))
        # print(list)

        line_chart = pygal.StackedLine()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = dataframe['dob'].tolist()
        line_chart.add('dt', dataframe['idno'].tolist())
        return Response(response=line_chart.render(),
                        content_type='image/svg+xml')
    else:
       return render_template('search.html')































@app.route("/analysis")
def analysis():
    return render_template('graph.html')


@app.route("/graph1")
def graph1():
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#53E89B',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        opacity='.6',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))
    dataframe = \
        pandas.read_sql_query("SELECT gender,count(gender) FROM emp_details GROUP BY gender",conn)
    print(dataframe)

    pie = pygal.Bar()
    pie.title = "Gender Distribution in %"
    pie.add(dataframe['gender'].tolist()[0],
            dataframe['count'].tolist()[0])

    pie.add(dataframe['gender'].tolist()[1],
            dataframe['count'].tolist()[1])

    return Response(response=pie.render(),
                    content_type='image/svg+xml')

@app.route("/graph2")
def graph2():
    hist = pygal.Histogram()
    hist.add('X', [(5, 0, 10), (4, 5, 13), (2, 0, 15)])
    hist.add('Y', [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)])
    return Response(response=hist.render(),
                    content_type='image/svg+xml')




@app.route("/graph3")
def graph3():
    dataframe = pandas.read_sql_query("SELECT emp_details.idno,emp_details.dob,emp_salary.amount,emp_salary.pay_date FROM emp_details INNER JOIN emp_salary ON emp_details.idno=emp_salary.idno",conn)
    print(dataframe)
    line_chart = pygal.StackedLine(fill=True)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = dataframe['dob'].tolist()
    line_chart.add('SALARY', dataframe['amount'].tolist())
    return Response(response=line_chart.render(),
                    content_type='image/svg+xml')

@app.route("/details")
def details():

    dataframe = \
         pandas.read_sql_query("SELECT * FROM emp_details"

                               ,conn)
    # come up your own data/sql/excel
    # analyze
    # visualize the data, 2 graphs
     # selecting specific columns
     # convert a specfic colm to list
     #print(dataframe['fname'].tolist())
     #print(dataframe['amount'].mean())
     #print(dataf


    # rame['amount'].describe())
    #print(dataframe.shape)  rows/colms
    # print(dataframe.ndim)
    print(dataframe['fname'].head(20))
    # matplotlib, seaborn, pygal,
    return render_template('details.html', data = dataframe)



if __name__ == '__main__':
    app.run(port=8000)

