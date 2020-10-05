
#Title : Write a Python Program to read from a csv file and write to a sql database!
#Descripstion : Generating Schema | Connection to SQL | Read CSV | Add table | Import Csv data to SQL
#Company : Kugelblitz Pvt. LTd.
#Author : Harsh Verma
#Date: 23 September 2020 

import mysql.connector as sql # LIbrary to connect to SQL and generate QUERY
import os #Access the OS Resources
from csv import reader


# connecting to database | using local server (localhost) 
# user information and credentials
# initial database connection | it can be set later using cursor (Line21) command also new database can be created 

endpoint = 'database-1.cwin0tpvvr05.us-east-2.rds.amazonaws.com'
username = 'admin'
password = 'pizza123aws'
database_name = 'test'

mydb = sql.connect(host=endpoint,
  user=username,
  password=password,
  database=database_name
)

# prints successfull completion of connecting sql 
print(mydb)


# cursor.execute --> to run command in sql shell
point = mydb.cursor()

# defining a function create_table() ---> executes a CREATE TABLE query using cursor command
def create_table():    
    try:
        # table name is static 
        point.execute("CREATE TABLE movie (MovieId int(100) not null auto_increment primary key,Year int(100),Score int(100),Title varchar(100))")

    # IF already created exception message will be thrown
    except sql.Error as err:
        if err.errno == sql.errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            # if any other error occurs | it will be printed as it is 
            print(err.msg)

# calling fuction create_table()
create_table()

# executes SHOW TABLE commands
point.execute("SHOW TABLES") 

# loop that PRINTS all the TABLE NAMES 
for x in point:
    print(x)

#Hardik's Code

# Reading CSV file into dataframe
filee = (r'C:\Users\hArSH\Desktop\Kugelblitz\deniro.csv')

# Declaring list in which row-wise data is stored
a =[]

# To read dataset
with open(filee, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        a.append(row)  # Data is appended to list | it changes dtype of stored data from dataframe to list 

# Loop programmed to recursively call INSERT command
for row in range(1 ,len(a)-1):
    point.execute(f"INSERT INTO movie (Year,Score,Title) values({a[row][0]},{a[row][1]},{a[row][2]});")

# Commit changes in SQL database
mydb.commit()

# To load saved table 
point.execute("Select * from movie")

# loop that prints loaded data
for x in point:
    print(x)
print("%d"%point.rowcount)  

#Hardik's Code

# ----------------------------------------------------------- END ------------------------------------------
