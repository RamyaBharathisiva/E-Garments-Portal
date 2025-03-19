#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from wholesaler"""
cur.execute(q)
rec = cur.fetchall()

print("""
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
    <style>
        *{
            margin: 0;
            padding:0;
            box-sizing: border-box;
            font-family: sans-serif;
        }
        body{
            
        }
        .container{
            height: 100%;
            width:250px;
            position: absolute;
            background: #161616;
            z-index:1;
            transition: 0.5s ease;
            transform: translateX(-250px);
        }
        .container #head{
            color:antiquewhite;
            font-size: 30px;
            font-weight: bold;
            padding: 30px;
            text-transform: uppercase;
            letter-spacing: 5px;
            background-image: linear-gradient(30deg,#df0155,#ed4901);
            margin-left: 20px;

        }
        #head:hover{
            color:rgb(37, 24, 24);
        }
        ol{
            width:100%;
            list-style:none;
        }
        ol li{
            display: block;
            width: 100%;
        }
        ol li a{
            color:#fbfdce;
            padding: 15px 10px;
            text-decoration: none;
            display: block;
            font-size: 20px;
            letter-spacing: 1px;
            position: relative;
            transition: 0.3s;
            overflow: hidden;
            text-transform: capitalize;           
        }
        ol li a i{
            width:70px;
            font-size: 25px;
            text-align: center;
            padding-left: 30px;

        }
        ol li:hover a{
            background: #030303;
            color: #00eaff;
            letter-spacing: 5px;
            text-decoration: none;
        }
        #whole{
            margin-top: 40px;
        }
        #side{
            margin-top: 20px;
        }
        #check{
            -webkit-appearance: none;
            visibility: hidden;
            display: none;
        }
        span{
            position: absolute;
            right:-40px;
            top:30px;
            font-size: 25px;
            border-radius:3px;
            color:#fff;
            padding:3px 8px;
            cursor:pointer;
            background: #850000;
        }
        #bars{
            background: red;
        }
        #check:checked ~ .container{
            transform: translateX(0);
        }
        #check:checked ~ .container #bars{
            display: none;
        }
        #checked:checked ~ section{
            transform: scale(1.2);
            filter:brightness(20%);
        }
        #brand{
            color:white;
        }
        .navbar-inverse #brand:hover{
            color:red;
            word-spacing:2px;
        }
        .navbar-inverse #log{
            color:white;  
        }
        .navbar-inverse #log:hover{
            color:red;
            letter-spacing:1px;
        }
        .section{
            width: 100%;
            padding: 20px;
            min-width: 100vh;

        }   
        .tabular--wrapper{
            background: #fff;
            margin-top: 1rem;
            border-radius: 10px;
        }
        
        .table-container{
            width:100%;
            border-collapse: collapse;
            overflow-y: auto;
            height: 90vh;
        }
        
        th{
            padding: 15px;
            text-align:left;
        }
        tbody{
            background:#f2f2f2;
        }
        td{
            padding:15px;
            font-size:14px;
            color:black;
        }
        tr:nth-child(even){
            background-color:#fff ;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <nav class="navbar navbar-inverse" style="font-size: 10px;">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynav">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a href="homepage.html" class="navbar-brand" id="brand">Style Sphere</a>
                </div>
                <div class="collapse navbar-collapse" id="mynav">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="home.py" id="log" style="font-size:20px;">Logout</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <input type="checkbox" name="" id="check">
       <div class="container" style="margin-top: -20px;">
            <label for="check">
                <span class="fas fa-times" id="times"></span>
                <span class="fas fa-bars" id="bars"></span>        
            </label>
            <div></div>
            <div class="head"><a href="adminhome.py" style="text-decoration: none;" id="head">Admin</a></div>
            <ol>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="whole">Wholesaler <span class="caret" style="color: white;"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="newwholesaler.py">New User</a></li>
                        <li><a href="existingwholesaler.py">Existing User</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User</a>
                    <ul class="dropdown-menu">
                        <li><a href="newuser.py">New User</a></li>
                        <li><a href="existinguser.py">Existing User</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Employee</a>
                    <ul class="dropdown-menu">
                        <li><a href="addemployee.py">Add Employee</a></li>
                        <li><a href="existingemployee.py">Existing Employee</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Product<span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="newproduct.py">New Product</a></li>
                        <li><a href="existingproduct.py">Existing Product</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Offers</a>
                    <ul class="dropdown-menu">
                         <li><a href="addoffers.py">Add Offers</a></li>
                         <li><a href="existingoffers.py">Existing Offers</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="order.py" id="side">New Orders</a></li>
                         <li><a href="exorder.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Wholesaler Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="newwholeorder.py" id="side">New Orders</a></li>
                         <li><a href="exwholeorders.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User Design Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="userdesign.py" id="side">New Orders</a></li>
                         <li><a href="exuserdesign.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Wholesaler Design Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="wholedesign.py" id="side">New Orders</a></li>
                         <li><a href="exwholedesign.py">Existing Orders</a></li>
                    </ul>
                </li>
                
            </ol>
        </div>
        </div>

        <div class="tabular-wrapper" >
            <h3 class="min-title" style="font-size: 29px;margin-left:100px;"><b>New Wholesaler Details</b></h3>
            <div class="table-container">
                <table class="table">
                        <tr>
                            <th>id</th>
                            <th>Wholesaler name</th>
                            <th>Gender</th>
                            <th>Emailid</th>
                            <th>DOB</th>
                            <th>Phone number</th>
                            <th>Photo</th>
                            <th>Shop Name</th>
                            <th>Shop Licence</th>
                            <th>Shop Image</th>
                            <th>Aadhaar card</th>
                            <th>Address</th>
                            <th>Approve</th>
                            <th>Delete</th>
                        </tr>
      """)
for i in rec:
    fn1 = "dbmedia/" + i[6]
    fn2 = "dbmedia/" + i[8]
    fn3 = "dbmedia/" + i[8]
    fn4 = "dbmedia/" + i[9]
    if i[18] != 'Approved' and i[18] != 'Discard':
        print("""
                                    <tr>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td><img src="%s" alt="img" width="100px" height="100px"></td>
                                        <td>%s</td>
                                        <td><img src="%s" alt="img" width="100px" height="100px"></td>
                                        <td><img src="%s" alt="img" width="100px" height="100px"></td>
                                        <td><img src="%s" alt="img" width="100px" height="100px"></td>
                                        <td>%s,%s\n%s,\n%s,%s,\n%s</td>
                                        <td>
                                                <form method="post" enctype="multipart/form-data">
                                                    <input type="hidden" name="emailid" value="%s">
                                                    <input type="hidden" name="ownername" value="%s">
                                                    
                                                    <input type="submit" name="approve" class="btn btn-success" value="Approved">
                                                </form>
                                        </td>
                                        <td>
                                                <form method="post" enctype="multipart/form-data">
                                                    <input type="hidden" name="id" value="%s">
                                                    <input type="submit" name="discard" class="btn btn-danger" value="Discard">
                                                    
                                                </form>
                                        </td>
                                    </tr>
              """ %(i[0],i[1],i[2],i[3],i[4],i[5],fn1,i[7],fn2,fn3,fn4,i[11],i[12],i[13],i[14],i[15],i[16],i[3],i[1],i[0]))

form = cgi.FieldStorage()
emailid=form.getvalue("emailid")
ownername=form.getvalue("ownername")
id=form.getvalue("id")
approve = form.getvalue("approve")
discard = form.getvalue("discard")

if approve != None:
        q1 = """Select max(id) from wholesaler"""
        cur.execute(q1)
        rec = cur.fetchone()
        if rec[0] != None:
            n = rec[0]
        else:
            n = 0
        z = ""
        if n <= 9:
            z = "000"
        elif n == 10 or n <= 99:
            z = "00"
        elif n > 99 or n <= 999:
            z = "0"
        uniquepass = "style" + z + "S" + str(n + 1)
        q2 = """Update wholesaler set password="%s" where email="%s" """%(uniquepass,emailid)
        print(q2)
        cur.execute(q2)
        fromadd = "ramyabharathi.242002@gmail.com"
        password = "oshiotvoqktvvjpa"
        toadd = emailid
        subject = "Welcome to StyleSphere!!!"
        body = "Hi! {}, Your profile has been approved,Use this to login to your account,\n\n\nYour username:{}\nYour password:{}".format(ownername,ownername,uniquepass)
        msg = "subject: {}\n\n{}".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, password)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        q3 = """Update wholesaler set status="%s" where email="%s" """ % (approve, emailid)
        cur.execute(q3)
        con.commit()
        print("""
                <script>
                    alert("Approved Successfully");
                </script>
        """)

if discard != None:
        q = """Update wholesaler set status = "%s" where id="%s" """ %(discard,id)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Discard Successfully");
        </script>
        """)




