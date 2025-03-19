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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        form {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
            border-radius: 8px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        input[type="text"],
        input[type="email"],
        input[type="password"],
        input[type="number"],
        input[type="date"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        input[type="radio"] {
            margin-right: 5px;
        }

        input[type="submit"] {
            background-color: #4caf50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 18px;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form name="login" id="login" method="post" enctype="multipart/form-data">
        <div class="form-group" style="margin-left: 77px;">
            <input type="text" id="username" name="username" placeholder="Username" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Gender<input type="radio" id="ugender" name="ugender" style="margin-left: 20px;">
            Male<input type="radio" id="ugender" name="ugender" style="margin-left: 20px;">
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
udoor=form.getvalue('udoor')
ustreet=form.getvalue('ustreet')
ucity=form.getvalue('ucity')
udistrict=form.getvalue('udistrict')
ustate=form.getvalue('ustate')
upincode=form.getvalue('upincode')
if usubmit != None:
        w="""insert into user(username,gender,email,dob,password,phno,door,street,city,district,state,pincode) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(uusername,ugender,uemail,udob,upassword,uphno,udoor,ustreet,ucity,udistrict,ustate,upincode)
        cur.execute(w)
        con.commit()
        print("""
                            <script>
                                alert("Registered successfully!!")
                            </script>
                     """)