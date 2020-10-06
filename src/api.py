#Title : To Make a Basic Flask App
#Descripstion : Example for flask Api Deployement | Printing String output on main page 
#Company : Kugelblitz Pvt. LTd.
#Author : Harsh Verma
#Date: 25 September 2020 

# Importing flask library | mysql.connector library for connectivity to sql database
from flask import Flask, request, jsonify
import mysql.connector as sql


# Creates the Flask application object, which contains data about the application and also methods
app = Flask(__name__)
# Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app.
app.config["DEBUG"] = True

# generate and store query values in and table description in  an dictionary variable !
def dict_factory(cursor, row):
    d = {}
    # cursor.dercription consists information about table 
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]
    return d

# sql.connect --> used to establish connectivity with SQL server 

endpoint = 'database-1.cwin0tpvvr05.us-east-2.rds.amazonaws.com'
username = 'admin'
password = 'pizza123aws'
database_name = 'test'

conn= sql.connect(host=endpoint,
  user=username,
  password=password,
  database=database_name
)

# initial route 
@app.route('/', methods=['GET'])
def home():
    return "<h1>LIST OF  MOVIE </h1><p>A prototype API to display Movie critic data</p>"

# if 404 errorcde encountered // this finction executes 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# returns sql value result in JSON format on ( /all ) route
@app.route('/all', methods=['GET'])
def api_all():
    # data stores in dictionary
    conn.row_factory = dict_factory
    # dictionary = true --> returns column name along with values 
    cur = conn.cursor(dictionary=True)

    # Custom query to be executed 
    cur.execute('SELECT * FROM movie')
    # fetchall() retrieves query result and jasonify formats it into JSON format
    all_movies= cur.fetchall()
    return jsonify(all_movies)

@app.route('/year', methods=['GET'])
#def api_filter():
def qYear():
    # extracts parameter from api requests 
    query_parameters = request.args
    Year = query_parameters.get('year' or 'Year')


    # dictionary = true --> returns column name along with values 
    cur = conn.cursor(dictionary=True)

    # Custom query to be executed 
    query = "SELECT Title AS 'Movie.Title',Score AS 'Movie.Score' FROM movie WHERE"

    # appends query specifications according to conditions 
    to_filter = []
    if  Year or Year :
        query += ' year='
        to_filter.append(Year)
    if not ( Year or Year ):
        return page_not_found(404)

    query=query+to_filter[0]
    # data stores in dictionary
    conn.row_factory = dict_factory
    cur.execute(query)

    # fetchall() retrieves query result and jasonify formats it into JSON format
    results = cur.fetchall()
    return jsonify(results)

@app.route('/title', methods=['GET'])
def qTitle():
    # extracts parameter from api requests 
    query_parameters = request.args
    Title = query_parameters.get('title')

    # dictionary = true --> returns column name along with values 
    cur = conn.cursor(dictionary=True)

    # Custom query to be executed 
    query = "SELECT Year FROM movie where"

    # appends query specifications according to conditions 
    to_filter = []
    if Title:
        query += ' Title like '
        to_filter.append(f"'%{Title}%'")
    if not ( Title ):
        return page_not_found(404)


    query=query+to_filter[0]
    # data stores in dictionary
    conn.row_factory = dict_factory
    cur.execute(query)

    # fetchall() retrieves query result and jasonify formats it into JSON format
    results = cur.fetchall()
    return jsonify(results)


if __name__ == '__main__':
    # A method that runs the application server.
    app.run()
