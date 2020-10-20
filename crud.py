import mysql.connector 
from datetime import datetime
now_time = datetime.now()
def fetchStudent():
    try:
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="practice")#established connection between your database  
        mycursor=mysqldb.cursor()#cursor() method create a cursor object  
        mycursor.execute("select * from students")#Execute SQL Query to select all record   
        result = mycursor.fetchall() #fetches all the rows in a result set
        return result 
    except:   
        print('Error:Unable to fetch data.')  
        mysqldb.close()#Connection Close 

def createStudent(pass_data):
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="practice")#established connection between your database  
    mycursor=mysqldb.cursor()#cursor() method create a cursor object
    # print(pass_data)
    try:  
    #Execute SQL Query to insert record
        
        formatted_date = now_time.strftime('%Y-%m-%d %H:%M:%S')
        name=pass_data['name']
        dob=pass_data['dob']
        student_id=pass_data['student_id']
        datetime=formatted_date
        mobilenumber=pass_data['mobilenumber']
        sql_query = "INSERT INTO students (`name`, `dob`, `student_id`, `datetime`, `mobilenumber`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(name, dob, student_id, datetime, mobilenumber)
        mycursor.execute(sql_query)  
        mysqldb.commit() # Commit is used for your changes in the database
        return "Record inserted successfully..."   
    except:  
    # rollback used for if any error   
        mysqldb.rollback()  
        mysqldb.close()#Connection Close
        return "Failed"

def updateStudent(pass_data):
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="practice")#established connection between your database  
    mycursor=mysqldb.cursor()#cursor() method create a cursor object
    # print(pass_data)
    try:  
    #Execute SQL Query to insert record
        name=pass_data['name']
        dob=pass_data['dob']
        student_id=pass_data['student_id']
        mobilenumber=pass_data['mobilenumber']
        sql_query = "UPDATE students SET `name`='{0}', `dob`='{1}', `mobilenumber`='{2}'  WHERE `student_id`='{3}'".format(name, dob, mobilenumber, student_id)
        mycursor.execute(sql_query)  
        mysqldb.commit() # Commit is used for your changes in the database 
        return "Record updated successfully..."   
    except:  
    # rollback used for if any error   
        mysqldb.rollback()  
        mysqldb.close()#Connection Close
        return "Failed"

def deleteStudent(student_id):
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="practice")#established connection between your database  
    mycursor=mysqldb.cursor()#cursor() method create a cursor object
    try:  
    #Execute SQL Query to insert record
        sql_query = "DELETE FROM students WHERE student_id={0}".format(student_id)
        mycursor.execute(sql_query)  
        mysqldb.commit() # Commit is used for your changes in the database
        return "Record Deleted successfully..."  
    except:  
    # rollback used for if any error 
        mysqldb.rollback()  
        mysqldb.close()#Connection Close
        return "Failed"

output = fetchStudent()
# return_data = {}
# for x in output:
#     lst = {'name':x[1], 'dob':x[0], 'student_id':'1017', 'mobilenumber':'1234567890'}
#     print(x[0])
# print(output)

# pass_data = {'name':'Vijay176', 'dob':'1991-08-05', 'student_id':'1017', 'mobilenumber':'1234567890'}
# createStudent(pass_data)
# updateStudent(pass_data)
# student_id=100
# deleteStudent(student_id)
# k = 0
# lst = {}
# final_list = []
# for i in output:
#     print(output[k][1])
#     # lst = {}
#     # lst['name'] = i[1]
#     # lst['dob'] = str([2])
#     # lst['student_id'] = [3]
#     # lst['mobilenumber'] = [5]
#     k = k+1;
    # final_list.append(lst)
# print(final_list)