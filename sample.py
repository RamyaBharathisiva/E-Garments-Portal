#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()



print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" type="text/css" href="home.css" />    <script src="home.js"></script>
</head>
<body>
<form action="userhome.py" name="login" id="login" onsubmit="useraccount()" method="post" enctype="multipart/form-data">
                            <div class="form-group" style="margin-left: 77px;">
                                <input type="text" name="username" placeholder="Username" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Gender<input type="radio" id="ugender" name="ugender" style="margin-left: 20px;" value="Male">
                                Male<input type="radio" id="ugender" name="ugender" style="margin-left: 20px;" value="female">
                                Female
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="email" id="uemail" name="uemail" placeholder="Emailid" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="date" id="udob" name="udob" placeholder="DOB" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="password" id="upassword" name="upassword" placeholder="password" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="password" id="ucpassword" name="ucpassword" placeholder="Confirm password" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="number" id="uphno" name="uphno" placeholder="phone number" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="udoor" id="udoor" placeholder="Door Number" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="ustreet" id="ustreet" placeholder="street" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="ucity" id="ucity" placeholder="City" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="udistrict" id="udistrict" placeholder="District" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="ustate" id="ustate" placeholder="State" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="number" name="upincode" id="upincode" placeholder="Pincode" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="submit" class="btn btn-success" name="usubmit" value="Register" style="width:30%;width: 400px;">
                            </div>
                        </form>
      </body>
                  </html>""")

form = cgi.FieldStorage()
usubmit = form.getvalue("usubmit")
uusername = form.getvalue("username")
ugender = form.getvalue("ugender")
uemail = form.getvalue("uemail")
udob = form.getvalue("udob")
upassword = form.getvalue("upassword")
uphno = form.getvalue("uphno")
uaddress = f"{form.getvalue('udoor')},{form.getvalue('ustreet')},{form.getvalue('ucity')},{form.getvalue('udistrict')},{form.getvalue('ustate')},{form.getvalue('upincode')}"
if usubmit != None:
    if len(form) != 0:
        q="""INSERT INTO user(username,gender, email, dob, password, phno, address) VALUES('%s','%s','%s','%s','%s','%s','%s')"""%(uusername,ugender,uemail,udob,upassword,uphno,uaddress)
        cur.execute(q)
        con.commit()
        print("""
                            <script>
                                alert("Registered successfully!!")
                            </script>
        """)