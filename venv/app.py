from audioop import rms
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from mailbox import Message
from unittest import result
from flask import Flask, render_template, request,session
from flask import Flask, render_template, json, request
#from flask_mysqldb import MySQL
#from werkzeug import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, jsonify, url_for
import pymysql
import sys
import json
import random
import pymysql.cursors
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from flask import flash
from werkzeug.utils import secure_filename
#from werkzeug import secure_filename
from flask import Flask, session, redirect, url_for, request
#from settings import PROJECT_ROOT
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import mysql.connector
app = Flask(__name__)

#UPLOAD_FOLDER = url_for('static',='/uploads')
UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'mp3'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='employee_management',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587  # Use appropriate port for your email server
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'



# Function to send email
def send_email(recipient, subject, body):
    try:
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        mail.send(msg)
        return True
    except Exception as e:
        print(str(e))
        return False



def send_email(recipient_email, subject, message):
    # Configure the email server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Change to the appropriate port for your SMTP server
    sender_email = 'testmailalert20@gmail.com'
    sender_password = 'qwghdvduxumxjidk'

    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Create SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)



@app.route('/')
def student():
   return render_template('index.html')

@app.route('/showusersignin',methods = ['POST', 'GET'])
def showusersignin():
    return render_template("usersignin.html",result = result)


@app.route('/services',methods = ['POST', 'GET'])
def services():
    return render_template("services.html",result = result)

@app.route('/contactus',methods = ['POST', 'GET'])
def contactus():
    return render_template("contactus.html",result = result)



@app.route('/showuserhome',methods = ['POST', 'GET'])
def showuserhome():
    return render_template("userhome.html",result = result)



@app.route('/logout',methods = ['POST', 'GET'])
def logout():
    try:
        return render_template("index.html")
    except Exception as e:
        return json.dumps({'error': str(e)})
    

@app.route('/get_employee_name', methods=['POST'])
def get_employee_name():
    data = request.get_json()
    email = data.get('email')
    connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ename FROM addemployee WHERE email = %s"
            cursor.execute(sql, (email,))
            employee = cursor.fetchone()
        if employee:
            return jsonify(ename=employee['ename'])
        return jsonify(ename='')
    finally:
        connection.close()



# Define a route to render the attendance form
@app.route('/attendance', methods=['GET'])
def attendance_form():
    return render_template('attendance.html')

@app.route('/addsalary', methods=['GET'])
def addsalary():
    connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM addemployee"
            cursor.execute(sql)
            employees = cursor.fetchall()
        return render_template('salarydetail.html', employees=employees)
    finally:
        connection.close()


@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    try:
        aid = request.form['aid']
        dat = request.form['dat']
        status = request.form['status']
        reason = request.form.get('reason', '')  # Get reason if provided, otherwise default to empty string

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "INSERT INTO attendance (aid, dat, status, reason) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (aid, dat, status, reason))
            connection.commit()

        return redirect(url_for('attendance_form'))
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/viewemployee',methods = ['POST', 'GET'])
def viewemployee():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from addemployee"
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template("adminviewusers.html",data=data,id=0)
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/viewemployee/<int:id>',methods = ['POST', 'GET'])
def aedituser(id):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from addemployee"
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template("adminviewusers.html",data=data,id=id)
    except Exception as e:
        return json.dumps({'error': str(e)})
    

@app.route('/updateemployee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    if request.method == 'POST':
        # Extract data from the form
        id = request.form['id']  # Renamed to avoid conflict with function argument
        ename = request.form['ename']
        addr = request.form['addr']
        mbl = request.form['mbl']
        dob = request.form['dob']
        email = request.form['email']
        psw = request.form['psw']
  

        try:
            connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                # Update the allotment details in the database
                sql = "UPDATE addemployee SET id=%s, ename=%s, addr=%s, mbl=%s, dob=%s,  email=%s, psw=%s  WHERE id=%s"
                cursor.execute(sql, (id, ename, addr, mbl, dob, email, psw, id))
                connection.commit()
                flash('Add Employee details updated successfully', 'success')
                return redirect('/viewemployee')
                
                #return render_template("viewallocation.html", data=data)
        except Exception as e:
            print(str(e))
            flash('Error updating employee details', 'error')
        finally:
            connection.close()


    # Fetch allotment details from the database based on the ID
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM addemployee WHERE id=%s"
            cursor.execute(sql, id)
            employee_details = cursor.fetchone()
    except Exception as e:
        print(str(e))
        employee_details = {}
    finally:
        connection.close()

    return render_template("updateemployee.html", employee_details= employee_details, employrr_id=id)


@app.route('/adeleteuser/<int:id>', methods=['GET'])
def delete_employee(id):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "DELETE FROM addemployee WHERE id=%s"
            cursor.execute(sql, id)
            connection.commit()
            return redirect('/viewemployee')
    except Exception as e:
        print(str(e))
        return "An error occurred while deleting data."
    finally:
        connection.close()



@app.route('/ashow2',methods = ['POST', 'GET'])
def ashow2():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from attendance"
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template("viewattendance.html",data=data,aid=0)
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/ashow2/<int:aid>',methods = ['POST', 'GET'])
def aeditcomplaint(aid):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from attendance"
            cursor.execute(sql)
            connection.commit()
            data = cursor.fetchall()
            return render_template("viewattendance.html",data=data,aid=aid)
    except Exception as e:
        return json.dumps({'error': str(e)})



@app.route('/deleteuser/<int:aid>', methods=['GET'])
def delete_user(aid):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "DELETE FROM attendance WHERE aid=%s"
            cursor.execute(sql, aid)
            connection.commit()
            return redirect('/ashow2')
    except Exception as e:
        print(str(e))
        return "An error occurred while deleting data."
    finally:
        connection.close()

@app.route('/userviewemployee',methods = ['POST', 'GET'])
def userviewemployee():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from addemployee WHERE email=%s"
            cursor.execute(sql,session['email'])
            data = cursor.fetchall()
            return render_template("mydetails.html",data=data,id=0)
    except Exception as e:
        return json.dumps({'error': str(e)})
    


@app.route('/showadminsignin',methods = ['POST', 'GET'])
def showadminsignin():
    return render_template("adminsignin.html",result = result)

@app.route('/showsignup',methods = ['POST', 'GET'])
def showsignup():
    return render_template("signup.html",result = result)



@app.route('/asigninclick',methods = ['POST', 'GET'])
def asigninclick():
   if request.method == 'POST':
      try:
          email = request.form["email"]
          pwd = request.form["pwd"]
          # validate the received values
          if email and pwd:
              connection = pymysql.connect(host='localhost',
                                           user='root',
                                           password='',
                                           db='employee_management',
                                           charset='utf8mb4',
                                           cursorclass=pymysql.cursors.DictCursor)
              with connection.cursor() as cursor:
                  # Read a single record
                  #res = "select * from signup where email=%s and pwd=%s"
                  sql = "select * from adminlogin where user=%s and psw=%s"
                  cursor.execute(sql, (email, pwd))
                  res = cursor.fetchall()
                  if len(res) == 1:
                      connection.commit()
                      #connection.close()
                      return render_template('adminhome.html')

                  else:
                      error ="Invalid login"
                      connection.commit()
                    #  connection.close()
                      return "Invalid login"

      except Exception as e:
          return json.dumps({'error': str(e)})



@app.route('/usigninclick', methods=['POST', 'GET'])
def usigninclick():
    if request.method == 'POST':
        try:
            p1 = request.form["p1"]
            p2 = request.form["p2"]
            # Validate the received values
            if p1 and p2:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT id FROM addemployee WHERE email = %s AND psw = %s"
                    cursor.execute(sql, (p1, p2))
                    res = cursor.fetchone()  # Assuming there's only one matching record

                    if res:  # If a matching record is found
                        session['email'] = p1
                        session['id'] = res['id']  # Store the id in session
                        connection.commit()
                        return render_template('userhome.html')
                    else:
                        error = "Invalid login"
                        return "Invalid login"
        except Exception as e:
            return json.dumps({'error': str(e)})
    else:
        return "Method not allowed"




@app.route('/add_salary', methods=['POST'])
def add_salary():
    try:
        if request.method == 'POST':
            email = request.form['email']
            sdat = request.form['sdat']
            ename = request.form['ename']
            bs = request.form['bs']
            bonus = request.form['bonus']
            pf = request.form['pf']
            hra = request.form['hra']
            lic = request.form['lic']
            noofdays = request.form['noofdays']
            total = request.form['total']
            
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
                                         db='employee_management',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
       
            with connection.cursor() as cursor:
                sql = """INSERT INTO salary (email, sdat, ename, bs, bonus, pf, hra, lic, noofdays, total)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (email, sdat, ename, bs, bonus, pf, hra, lic, noofdays, total))
                connection.commit()
            return "Salary details added successfully"
        
    finally:
        connection.close()

# Route to render leave application form
@app.route('/apply_leave', methods=['GET'])
def leave_apply_form():
    return render_template('apply_leave.html')

# Route to handle leave application submission
@app.route('/apply_leave', methods=['POST'])
def leave_apply_submit():
    try:
        # Retrieve form data
        emp_id = request.form['emp_id']
        email = request.form['email']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        reason = request.form['reason']
        
        # Insert leave application into database
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "INSERT INTO leave_applications (emp_id,email, start_date, end_date, reason, status) VALUES (%s,%s, %s, %s, %s, %s)"
            cursor.execute(sql, (emp_id, email, start_date, end_date, reason, 'pending'))
            connection.commit()
        
        # Close connection
        connection.close()
        
        flash('Leave application submitted successfully!')
        return redirect(url_for('leave_apply_form'))
    except Exception as e:
        flash('Error occurred while submitting leave application: ' + str(e))
        return redirect(url_for('leave_apply_form'))



@app.route('/leave_application', methods=['GET'])
def admin_leave_applications():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Retrieve all leave applications from database
            sql = "SELECT * FROM leave_applications"
            cursor.execute(sql)
            leave_applications = cursor.fetchall()
    except Exception as e:
        flash('Error occurred while fetching leave applications: ' + str(e))
        return redirect(url_for('index'))
    finally:
        connection.close()
    
    return render_template('admin_leave_applications.html', leave_applications=leave_applications)

# Route to handle leave application approval/rejection
@app.route('/leave_application/<int:leave_id>/<action>', methods=['POST'])
def admin_handle_leave_application(leave_id, action):
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
      
            # Update leave application status in database
            sql = "UPDATE leave_applications SET status = %s WHERE id = %s"
            cursor.execute(sql, (action, leave_id))
            connection.commit()
        
        flash('Leave application ' + action + 'ed successfully!')
        return redirect(url_for('admin_leave_applications'))
    except Exception as e:
        flash('Error occurred while handling leave application: ' + str(e))
        return redirect(url_for('admin_leave_applications'))
    finally:
        connection.close()


# Route to handle leave application approval
@app.route('/leave_application/<int:lid>/approve', methods=['POST'])
def approve_leave_application(lid):
    email = request.form['email']
    return handle_leave_application(lid, email, 'approved')

# Route to handle leave application rejection
@app.route('/leave_application/<int:lid>/reject', methods=['POST'])
def reject_leave_application(lid):
    email = request.form['email']
    return handle_leave_application(lid,  email, 'rejected')

# Function to handle leave application approval/rejection
def handle_leave_application(lid, email, status):
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Update leave application status in database
            sql = "UPDATE leave_applications SET status = %s WHERE lid = %s"
            cursor.execute(sql, (status, lid))
            connection.commit()

             # Send email to the newly added employee
            subject = '  Leave Applications'
            message = f'Hi, Employee Management Details for the leave {email}  and  Status of your leave applications For your ID is {status}.'
            send_email(email, subject, message)

        flash(f'Leave application {status}ed successfully!')
    except Exception as e:
        flash('Error occurred while handling leave application: ' + str(e))
    finally:
        connection.close()
    
    return redirect(url_for('admin_leave_applications'))




@app.route('/userleave_applications', methods=['POST', 'GET'])
def userleave_applications():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from leave_applications WHERE emp_id=%s"
            cursor.execute(sql,session['id'],)
            data = cursor.fetchall()
            return render_template("user_leave_applications.html",data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})
    

@app.route('/viewscheme', methods=['POST', 'GET'])
def viewscheme():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from salary WHERE email=%s"
            cursor.execute(sql,session['email'],)
            data = cursor.fetchall()
            return render_template("viewsalary.html",data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/salarydetails')
def salarydetails():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='employee_management',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Fetch all employees from addemployee table
            sql = "SELECT email FROM addemployee"
            cursor.execute(sql)
            employees = cursor.fetchall()
    except Exception as e:
        # Handle any errors that occur during database query
        print("Error:", e)
        employees = []  # Empty list if there's an error
    finally:
        connection.close()

    return render_template('salarydetails.html', employees=employees)


@app.route('/addnote1', methods=['POST'])
def addnote1():
    try:
        id = request.form["id"]
        ename = request.form["ename"]
        addr = request.form["addr"]
        mbl = request.form["mbl"]
        dob = request.form["dob"]
        email = request.form["email"]
        job = request.form["job"]
        desin = request.form["desin"]
        psw = request.form["psw"]
       
        # validate the received values
        if ename and psw:
            try:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='employee_management',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    sql = "INSERT INTO addemployee (id,ename, addr, mbl, dob, email,job, desin, psw) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (id, ename, addr, mbl, dob, email, job, desin, psw))
                    connection.commit()
                    
                    # Send email to the newly added employee
                    subject = 'Employee Management Details'
                    message = f'Hi, Employee Management Details for the name {ename}  and  Password For your ID is {psw}.'
                    send_email(email, subject, message)
                    
                    flash('Employee Added Successfully')
                    return 'Employee Added Successfully'
            except Exception as e:
                print(str(e))  
                return json.dumps({'error': str(e)})
            finally:
                connection.close()
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/addnote',methods = ['POST', 'GET'])
def addnote():
    return render_template("addnote.html",result = result)



@app.route('/')
def index():
    # Generate the URL for the image
    gif = url_for('static', filename='images/vutura-chatbot.gif')
    return render_template("index.html", chat_gif=gif)  # Pass images to the template

@app.route('/adminhome',methods = ['POST', 'GET'])
def adminhome():
    return render_template("adminhome.html",result = result)




if __name__ == '__main__':
   app.secret_key = "sadfsdfdfssdfadsfsdfsd"
   app.run(port=5020)