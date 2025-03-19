#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from product where status="Approved" order by id DESC limit 5"""
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
    <link rel="stylesheet" type="text/css" href="home.css" />    <script src="home.js"></script>
    <style>
    img{
    height: 300px;
    width:300px;
}   
button{
    height: 40px;
    width:200px;
}

a>button{
    background-color: rgb(245, 62, 93);
    color: black;
    align-items: center;
}
button:hover{
    background-color: rgb(255, 137, 157);
}
a{
    text-decoration: none;  
}

    </style>
</head>
<body>
    <header class="navbar navbar-expand-sm">
        <nav class="navbar navbar" style="font-size: 10px;box-shadow: 0px 5px 20px -10px rgb(0, 0, 0);">
            <div class="container-fluid">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynav" style="margin-top: 30px;">
                        <span class="icon-bar" style="background-color:rgb(3, 3, 3);"></span>
                        <span class="icon-bar"  style="background-color:rgb(3, 3, 3);"></span>
                        <span class="icon-bar"  style="background-color:rgb(3, 3, 3);"></span>
                    </button>
                    <a href="home.py" class="navbar-brand mx-auto">
                        <img src="assets/Logo2.png" id="logo" alt="logo" class="navbar-brand">
                    </a>
                </div>
                <div class="collapse navbar-collapse" id="mynav">
                    <ul class="nav navbar-nav ml-auto" id="nav"> 
                        <li><a href="women.py" id="a"><b>Women</b></a></li>
                        <li><a href="mens.py" id="a"><b>Men</b></a></li>
                        <li><a href="kids.py" id="a"><b>Kids</b></a></li>
                        <li><a href="design.py" id="a"><b>Latest Launch</b></a></li>
                        <li><a href="#" id="sign" data-toggle="dropdown" style="color:black"><b>Sign in </b><span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="" data-toggle="modal" data-target="#modal"><b>Admin</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal2"><b>User</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal3"><b>Wholesaler</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal4"><b>Employee</b></a></li> 
                            </ul>
                        </li>
                        <li><a href="#" id="sign" data-toggle="dropdown" style="color:black"><b>Sign up </b><span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="" data-toggle="modal" data-target="#modal11" style="width: 100%;"><b>User</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal22" style="width: 100%;"><b>Wholesaler</b></a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div id="modal" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;">Admin login</h3></center>
                    </div>
                    <div class="modal-body">
                        <form action="adminhome.py" name="login" id="login" onsubmit="return validate()">
                            <div class="form-group">
                                <input type="text" name="user" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="pass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="submit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                    </div>
                </div>
            </div>
        </div>
        <div id="modal2" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;">User login</h3></center>
                    </div>
                    <div class="modal-body">
                        <form action="userhome.py" name="userlogin" id="userlogin" onsubmit="return ulvalidate()">
                            <div class="form-group">
                                <input type="text" name="user" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="pass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <a href="#" style="margin-left:300px;">forget password?</a>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="submit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                            New user?<a href="">Sign up</a>
                    </div>
                </div>
            </div>
        </div>
        <div id="modal3" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;">Wholesaler login</h3></center>
                    </div>
                    <div class="modal-body">
                        <form action="wholehome.py" name="login" id="login" onsubmit="return wlvalidate()">
                            <div class="form-group">
                                <input type="text" name="user" id="user" placeholder="Username" s+6+tyle="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="pass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <a href="#" style="margin-left:300px;">forget password?</a>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="submit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                            New user?<a href="" data-toggle="modal" data-target="modal22">Sign up</a>
                    </div>
                </div>
            </div>
        </div>
        <div id="modal4" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;">Employee login</h3></center>
                    </div>
                    <div class="modal-body">

                        <form action="employeehome.py" name="login" id="login" onsubmit="return elvalidate()">
                            <div class="form-group">
                                <input type="text" name="user" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="pass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="submit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                    </div>
                </div>
            </div>
        </div>
        <div id="modal11" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 20px;">User signup</h3></center>
                    </div>
                    <div class="modal-body">
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
                    </div>
                    <div class="modal-footer">
                        <label for="existing user">Existing user?<a href="" data-toggle="modal" data-target="#modal">login</a></label>
                    </div>
                </div>
            </div>
        </div>
        <div id="modal22" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3>Wholesaler signup</h3></center>
                    </div>
                    <div class="modal-body">
                        <form action="wholehome.py" name="wsignup" id="login" onsubmit="wholesaler()" method="post" enctype="multipart/form-data">
                            <div class="form-group" style="margin-left: 77px;">
                                <input type="text" name="ownername" placeholder="Owner Name" style="height: 40px;width:400px">

                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Gender<input type="radio" id="wgender" name="wgender" style="margin-left: 20px;" value="Male">
                                Male<input type="radio" id="ugender" name="wgender" style="margin-left: 20px;" value="Female">
                                Female
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="email" id="wemail" name="wemail" placeholder="Emailid" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="date" id="wdob" name="wdob" placeholder="DOB" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="number" id="wphno" name="wphno" placeholder="phone number" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Upload Your Photo<input type="file" name="wPhoto" id="wphoto" style="margin-top: 10px;">    
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" id="shopname" name="shopname" placeholder="Shopname" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Shop licence<input type="file" name="licence" id="licence" style="margin-top: 10px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Shop Image<input type="file" name="shopimage" id="shopimage" style="margin-top: 10px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                Aadhaar card<input type="file" name="aadhaar" id="aadhaar" style="margin-top: 10px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="wdoor" id="wdoor" placeholder="Door Number" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="wstreet" id="wstreet" placeholder="street" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="wcity" id="wcity" placeholder="City" style="height: 40px;width: 400px;">  
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="wdistrict" id="wdistrict" placeholder="District" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="text" name="wstate" id="wstate" placeholder="State" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="number" name="wpincode" id="wpincode" placeholder="Pincode" style="height: 40px;width: 400px;">
                            </div>
                            <div class="form-group" style="margin-left: 80px;">
                                <input type="submit" class="btn btn-success" name="wsubmit" value="Register" style="width:30%;width: 400px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <label for="existing user">Existing user?<a href="" data-toggle="modal" data-target="#modal2">login</a></label>
                    </div>
                </div>
            </div>
        </div>
    </header> 
    <div class="container-fluid">
            <h1><b>Latest Launch</b></h1>
            <hr>
            <br>
            <br>
            <div class="row">""")

for i in rec:
    fn = "product/" + i[3]
    print(""" <div class="col-md-3">
                            <img class="dress-card-img-top" src="%s" alt="img">
                            <h4 class="dress-card-title">%s</h4>
                            <p class="dress-card-para" style="color: rgb(218, 27, 59);">%s</p>
                            <p class="dress-card-para"><span class="dress-card-price">Rs.%s &ensp;</span></p>
                            <button type="button" class="btn" data-toggle="modal" data-target="#myModal" style="background-color: rgb(188, 37, 87);color:white;">
                                <b>BUY NOW</b>
                              </button>
                </div>""" % (fn, i[2], i[4], i[8]))

print("""    <div id="myModal" class="modal fade" role="dialog">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header" style="border:none;">

                                <a class="close" data-dismiss="modal"><b>x</b></a>
                            </div>
                            <div class="modal-body">
                                <p style="font-size:30px;">Welcome to StyleSphere!!</p>
                                <div class="row">
                                    <div class="col-md-3"></div>
                                    <div class="col-md-6">
                                        <p>To Access Account and Manage Orders Please Login Your Account</p> 
                                    </div>
                                    <div class="col-md-3"></div>                
                                </div>

                            </div>

                            <div class="modal-footer"style="border:none;"></div>
                        </div>
                    </div>
                </div>
""")

print("""

  """)

# !C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
x = """Select * from user where id = "%s" """ % (ID)
cur.execute(x)
recc = cur.fetchall()

q = """Select* from userdesign"""
cur.execute(q)
rec1 = cur.fetchall()

q = """SELECT user.username,user.door,user.street,user.city,user.district,user.state,user.pincode,user.phno,userdesign.quantity,userdesign.size,userdesign.price,userdesign.totalprice,userdesign.status,userdesign.id,userdesign.referenceimage,userdesign.dresstype,userdesign.userid FROM userdesign INNER JOIN user ON userdesign.userid = user.id where userdesign.userid="%s" AND userdesign.status!="NULL" AND receive!="Product Received" AND action = "Product Delivered" """ % ID
cur.execute(q)
rec = cur.fetchall()

q3 = """SELECT SUM(totalprice) FROM orders WHERE userid="%s" and status = "Confirm" """ % ID
cur.execute(q3)
total = cur.fetchone()

print("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="userhome.css">
    <style>

button{
    height: 40px;
    width:200px;
}

a>button{
    background-color: rgb(245, 62, 93);
    color: black;
    align-items: center;
}
button:hover{
    background-color: rgb(255, 137, 157);
}
a{
    text-decoration: none;  
}



    .text--container{
        color: rgba(82, 80, 80, 0.774);
        font-weight: 600;
    }
    .color{
        background-color: #fffefede;
        /* border: solid black 6px; */
        border-radius: 25px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

    .table th,td{
        border: hidden;
    }




.footer {
  background-color: black;
  color: white;
  margin-top: 600px;
}
li {
  list-style: none;
  font-size: 20px;
}
#p2 {
  font-size: 20px;
}
footer > a {
  text-decoration: none;
  color: white;
}
.social-links {
  font-size: 30px;
}


    </style>
    <script>
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}

</script>
</head>
<body>
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
   <a href="userlatest.py?id=%s" style="margin-top: 30px;color:rgb(231, 183, 120);"><b>Latest Launch</b></a>
   <div class="dropdown">
        <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Women</b><span class="caret"></span></a>
            <ul class="dropdown-menu">
                  <li><a href="userkurta.py?id=%s">kurtas kurtis</a></li>
                  <li><a href="user wbottom.py?id=%s">Bottom Wear</a></li>
                  <li><a href="userparty.py?id=%s">Party Dresses</a></li>
                  <li><a href="user wsports.py?id=%s">Sports Wear</a></li>
                  <li><a href="user wwinter.py?id=%s">Winter Wear</a></li>
            </ul>
   </div>
   <div class="dropdown">
            <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Men</b><span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="user mtop.py?id=%s">Top Wear</a></li>
                  <li><a href="user mbottom.py?id=%s">Bottom Wear</a></li>
                  <li><a href="user msports.py?id=%s">Sports Wear</a></li>
                  <li><a href="user mwinter.py?id=%s">Winter Wear</a></li>
                </ul>
   </div>  
   <div class="dropdown">                
            <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Kids</b><span class="caret"></span></a>
            <ul class="dropdown-menu">
                 <li><a href="user kids1.py?id=%s">Boys clothing</a></li>
                 <li><a href="user kids2.py?id=%s">Girls Clothing</a></li>
                 <li><a href="user kids3.py?id=%s">Baby Boys Clothing</a></li>
                 <li><a href="user kids4.py?id=%s">Baby Girls Clothing</a></li>
            </ul>
   </div>         
   <a href="udesign.py?id=%s" style="margin-top: 30px;color:rgb(231, 183, 120);"><b>Design</b></a>
   <a href="uoffers.py?id=%s" style="margin-top: 30px;"><b>Offers</b></a>
   <a href="ufeedback.py?id=%s" style="margin-top: 30px;"><b>Feedback</b></a>
</div>""" % (ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID))

print("""
<div id="main">
       <nav class="navbar navbar" style="font-size: 10px;box-shadow: 0px 5px 20px -10px rgb(0, 0, 0);">
        <div class="container-fluid">
                <span style="font-size:40px;cursor:pointer;" onclick="openNav()" id="open">&#9776;</span>
                <a href="" class="navbar-brand mx-auto">
                    <img src="assets/Logo2.png" id="logo" alt="logo" class="navbar-brand">
                </a>
                <div class="navbar-right">
                    <img src="assets/profile.png" alt="img" height="50px"style="margin-right:20px" data-toggle="dropdown">
                        <ul class="dropdown-menu">
                            <li><a href="uprofile.py?id=%s" data-toggle="modal" data-target="#modal"><b><i class="fas fa-edit"></i> Edit Profile</b></a></li>
                            <li><a href="uorders.py?id=%s"><b><i class="fa-solid fa-cart-shopping"></i> Orders</b></a></li>
                            <li><a href="udesignorders.py?id=%s"><b><i class="fa-solid fa-cart-shopping"></i> Design Orders</b></a></li>
                            <li><a href="home.py?id=%s"><b><i class="fa fa-sign-out" style="font-size:24px"></i> Logout </b></a></li>
                        </ul>
                </div>
        </div>
    </nav>""" % (ID, ID, ID, ID))
q2 = """Select username from user where id = "%s" """ % ID
cur.execute(q2)
name = cur.fetchone()
q4 = """Select door from user where id = "%s" """ % ID
cur.execute(q4)
address = cur.fetchone()
q6 = """Select street from user where id = "%s" """ % ID
cur.execute(q6)
address1 = cur.fetchone()
q7 = """Select city from user where id = "%s" """ % ID
cur.execute(q7)
address2 = cur.fetchone()
q8 = """Select district from user where id = "%s" """ % ID
cur.execute(q8)
address3 = cur.fetchone()
q9 = """Select state from user where id = "%s" """ % ID
cur.execute(q9)
address4 = cur.fetchone()
q10 = """Select pincode from user where id = "%s" """ % ID
cur.execute(q10)
address5 = cur.fetchone()

q5 = """Select phno from user where id = "%s" """ % ID
cur.execute(q5)
phno = cur.fetchone()
print("""   
        <div class="container-fluid">
            <h1><b>Your Designs</b></h1>
            <hr>
            <br>
            <br>
            <div class="row">
            <div class="col-md-2"></div>""")

for i in rec:
    if i[12] == "Approved":
        print("""
                <div class="col-md-8">
                        <div class="container mt-3">
                            <div class="row  text-capitalize color"><div class="col-lg-12 text--container mt-4">
                        <center><h1><b>Your Design is Approved!!</b></h1></center>
                        <div class="mt-4">
                            <form action="" method="post" enctype="multipart/form-data">
                                <div class="form-group">
                                        <label for="price">Price</label>
                                        <input type="number" id="price" name="price" value="%s"  class="form-control" readonly>
                                    </div>
                                    <div class="form-group">
                                        <label for="price">Total Price</label>
                                        <input type="text" id="totalprice" name="totalprice" value="%s" class="form-control" readonly>
                                    </div>
                                    <div class="form-group">
                                        <b>Payment method:</b><br>         
                                        <input type="radio" name="pay" id="radio1" class="form-check-input" value="credit or debit card"  checked>Credit or Debit card<label class="form-check-label" for="radio1"></label>
                                    </div>
                                    <div class="form-group">
                                                    <b>Enter Card Number:</b>
                                                    <input type="number" name="card" class="form-control" required>

                                                    <input type="hidden" name="proid" value="%s">
                                                    <input type="hidden" name="name" value="%s">
                                                    <input type="hidden" name="category" value="%s">
                                                    <input type="hidden" name="quan" value="%s">
                                                    <input type="hidden" name="size" value="%s">
                                                    <input type="hidden" name="price" value="%s">
                                                    <input type="hidden" name="tprice" value="%s">
                                                    <input type="hidden" name="userid" value="%s">
                                    </div>
                                    <div class="form-group">
                                                    <b>Expiry Date:</b>
                                                    <input type="date" name="edate" class="form-control" required>
                                    </div>

                                    <input type="submit" name="accept" value="confirm Order">
                            </form>

                        </div>

                </div>


    """ % (i[10], i[11], i[13], i[15], i[15], i[8], i[9], i[10], i[11], i[16]))

order = form.getvalue("accept")
card = form.getvalue("pay")
cardno = form.getvalue("card")
exdate = form.getvalue("edate")
proid = form.getvalue("proid")
proname = form.getvalue("name")
category = form.getvalue("category")
quan = form.getvalue("quan")
size = form.getvalue("size")
price = form.getvalue("price")
prize = form.getvalue("tprice")
uid = form.getvalue("userid")

if order != None:
    if len(form) != 0:
        q11 = """INSERT INTO orders(productid, productname, category, quantity, size, price, totalprice, card, cardno, expirydate, userid)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
        proid, proname, category, quan, size, price, prize, card, cardno, exdate, uid)
        cur.execute(q11)
        con.commit()
        print("""
                    <script>
                        alert("Your order is placed");
                    </script>
                """)

#                 print("""
#                 <center><h2 class="mt-4"><b>Ordered Products</b></h2></center>
#                 <div class="col-md-12">
#
#                     <table class="table text-center">
#                         <tr>
#                             <th>Product</th>
#                             <th>ProductName</th>
#                             <th>Quantity</th>
#                             <th>Size</th>
#                             <th>Price</th>
#                             <th>Totalprice</th>
#                         </tr>
# """)
#
#                 fn = "design/" + i[14]
#                 print("""
#                         <tr>
#                             <td><img src="%s" alt="product" class="img-fluid" style="max-height: 100px;"></td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>
#                             <form method="post" enctype="multipart/form-data">
#                                 <input type="hidden" name="oid" value="%s">
#                                 <input type="submit" class="btn btn-primary" value="Product Received" name="receive">
#                             </form>
#                             </td>
#                         </tr>
#                         """ % (fn, i[15], i[8], i[9],i[10], i[11], i[13]))
#                 print("""
#                 <div class="container">
#                     <hr>
#                 </div>
#                 <div class="col-md-6"></div>
#                 <div class="col-md-6 mb-4">
#                     <table class="table text-center">
#
#                         <tr>
#                             <th>Delivered to: </th>
#                             <td>%s,%s,%s,%s,%s,%s</td>
#                         </tr>
#                         <tr>
#                             <th>Phone number: </th>
#                             <td>%s</td>
#                         </tr>
#                     </table>
#                 </div>
#             </div>
#             </div>
#         <div class="col-md-2"></div><br><br>
#         </div><br><br>
#           """ % (address[0], address1[0], address2[0], address3[0], address4[0], address5[0], phno[0]))
#     receive = form.getvalue("receive")
#     oid = form.getvalue("oid")
#
#     if receive != None:
#         q = """Update userdesign set receive="%s" where id="%s" """ % (receive, oid)
#         cur.execute(q)
#         con.commit()
#         print("""
#             <script>
#                 alert("Product received");
#             </script>
#         """)
#     elif i[12]=="Discard":
#         print("""
#     <div class="container mt-3">
#             <div class="row  text-capitalize color">
#             <div class="col-lg-12 text--container mt-4">
#                         Design Request is Denied!!
#                 </div>
#             </div>
#
#
#     """)


print("""

<footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <h4>WHO WE ARE</h4>
                    <ul>
                        <li><a href="#" style="color: white;">About us</a></li>
                        <li><a href="#" style="color: white;">Careers</a></li>
                        <li><a href="#" style="color: white;">Press</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h4>CUSTOMERS</h4>
                    <ul>
                        <li><a href="#" style="color: white;">help</a></li>
                        <li><a href="#" style="color: white;">size guide</a></li>
                        <li><a href="#" style="color: white;">how do i shop</a></li>
                        <li><a href="#" style="color: white;">how do i pay</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h4>SHOP BY</h4>
                    <ul>
                        <li><a href="#" style="color: white;">Men</a></li>
                        <li><a href="#" style="color: white;">Women</a></li>
                        <li><a href="#" style="color: white;">Kids</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h4>CONTACT US</h4>
                    <div class="social-links">
                        <a href="#" style="color: white;"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" style="color: white;"><i class="fab fa-twitter"></i></a>
                        <a href="#" style="color: white;"><i class="fab fa-instagram"></i></a>
                        <a href="#" style="color: white;"><i class="fab linked-in"></i></a>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                    <center><p id="p2"  style="margin-top: 50px;">&copy; 2024 StyleSphere. All rights reserved</p></center>
                </div>
            </div>
        </div>
    </footer>
""")



