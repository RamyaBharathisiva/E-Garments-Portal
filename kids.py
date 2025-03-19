#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from product where category = "kids" and status="Approved" """
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
    <link rel="stylesheet" type="text/css" href="home.css">   



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
                        <li><a href="latest.py" id="a"><b>Latest Launch</b></a></li>
                        <li><a href="#" id="sign" data-toggle="dropdown" style="color:black"><b>Sign in </b><span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="" data-toggle="modal" data-target="#modal"><b>Admin</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal2"><b>User</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal3"><b>Wholesaler</b></a></li>
                                <li><a href="" data-toggle="modal" data-target="#modal4"><b>Employee</b></a></li> 
                                <li><a href="" data-toggle="modal" data-target="#modal44"><b>Delivery Employee</b></a></li> 
                            </ul>
                        </li>
                        <li><a href="#" id="sign" data-toggle="dropdown" style="color:black;margin-right:40px;"><b>Sign up </b><span class="caret"></span></a>
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
                        <center><h3 style="font-size: 30px;"><b>Admin login</b></h3></center>
                    </div>
                    <div class="modal-body">
                        <form name="alogin" id="alogin" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <input type="text" name="auser" id="auser" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="apass" id="apass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="asubmit" id="asubmit" value="login" style="width:30%;margin-left: 195px;">
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
                        <center><h3 style="font-size: 30px;"><b>User login</b></h3></center>
                    </div>
                    <div class="modal-body">
                        <form  name="userlogin" id="userlogin" method="post" enctype="multipart/form-data" >
                            <div class="form-group">
                                <input type="text" name="user" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="pass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <a href="forgot.py" style="margin-left:300px;">forgot password?</a>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="ulsubmit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                            New user?<a href="" data-toggle="modal" data-target="#modal11">Sign up</a>
                    </div>
                </div>
            </div>
        </div>
        <div id="modal3" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;"><b>Wholesaler login</b></h3></center>
                    </div>
                    <div class="modal-body">
                        <form  name="login" id="login" method="post" enctype="multipart/form-data" >
                            <div class="form-group">
                                <input type="text" name="wuser" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="wpass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <a href="wforgot.py" style="margin-left:300px;">forgot password?</a>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="wlsubmit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                            New user?<a href="" data-toggle="modal" data-target="#modal22">Sign up</a>
                    </div>
                </div>
            </div>
        </div>
        <div id="modal4" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;"><b>Employee login1</b></h3></center>
                    </div>
                    <div class="modal-body">

                        <form  name="login" id="login" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <input type="text" name="euser" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="epass" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="esubmit" value="login" style="width:30%;margin-left: 195px;">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                    </div>
                </div>
            </div>
        </div>
         <div id="modal44" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3 style="font-size: 30px;"><b>Employee login2</b></h3></center>
                    </div>
                    <div class="modal-body">

                        <form  name="login" id="login" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <input type="text" name="euser2" id="user" placeholder="Username" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="password" name="epass2" id="pass" placeholder="Password" style="width: 50%;height: 40px;margin-left: 140px;"><br><br>
                            </div>
                            <div class="form-group">
                                <input type="submit" class="btn btn-success" name="esubmit2" value="login" style="width:30%;margin-left: 195px;">
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
                        <center><h3 style="font-size: 20px;"><b>User signup</b></h3></center>
                    </div>
                    <div class="modal-body">
                       <form name="signup" id="signup" method="post" enctype="multipart/form-data">
                                <div class="form-group" style="margin-left: 77px;">
                                    <input type="text" id="username" name="username" placeholder="Username" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Gender<input type="radio" id="ugender" name="ugender" value="male" style="margin-left: 20px;">
                                    Male<input type="radio" id="ugender" name="ugender" value="female" style="margin-left: 20px;">
                                    Female
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="email" id="uemail" name="uemail" placeholder="Emailid" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="date" id="udob" name="udob" placeholder="DOB" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="password" id="upassword" name="upassword" placeholder="password" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="password" id="ucpassword" name="ucpassword" placeholder="Confirm password" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="number" id="uphno" name="uphno" placeholder="phone number" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="udoor" id="udoor" placeholder="Door Number" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="ustreet" id="ustreet" placeholder="street" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="ucity" id="ucity" placeholder="City" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="udistrict" id="udistrict" placeholder="District" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="ustate" id="ustate" placeholder="State" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="number" name="upincode" id="upincode" placeholder="Pincode" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="submit" class="btn btn-success" name="usubmit" value="Register" style="width:30%;width: 400px;" required>
                                </div>
                        </form>
                        </div>
                        <div class="modal-footer">
                                <label for="existing user">Existing user?<a href="" data-toggle="modal" data-target="#modal2">login</a></label>
                        </div>
                </div>
            </div>
        </div>
        <script>
document.getElementById('wsignup').addEventListener('submit', function (event) {
    var ownername = document.getElementById('ownername').value;
    var wgender = document.querySelector('input[name="wgender"]:checked');
    var wemail = document.getElementById('wemail').value;
    var wdob = document.getElementById('wdob').value;
    var wphno = document.getElementById('wphno').value;
    var wphoto = document.getElementById('wphoto').value;
    var shopname = document.getElementById('shopname').value;
    var licence = document.getElementById('licence').value;
    var shopimage = document.getElementById('shopimage').value;
    var aadhaar = document.getElementById('aadhaar').value;
    var wdoor = document.getElementById('wdoor').value;
    var wstreet = document.getElementById('wstreet').value;
    var wcity = document.getElementById('wcity').value;
    var wdistrict = document.getElementById('wdistrict').value;
    var wstate = document.getElementById('wstate').value;
    var wpincode = document.getElementById('wpincode').value;

    // Basic validation
    if (!ownername || !wgender || !wemail || !wdob || !wphno || !wphoto ||
        !shopname || !licence || !shopimage || !aadhaar || !wdoor || !wstreet ||
        !wcity || !wdistrict || !wstate || !wpincode) {
        alert("Please fill in all required fields.");
        event.preventDefault();
        return false;
    }

    // Validate email format
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(wemail)) {
        alert("Please enter a valid email address.");
        event.preventDefault();
        return false;
    }

    // Validate phone number (10 digits)
    var phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(wphno)) {
        alert("Please enter a valid 10-digit phone number.");
        event.preventDefault();
        return false;
    }

    // Validate pincode (6 digits)
    var pincodeRegex = /^\d{6}$/;
    if (!pincodeRegex.test(wpincode)) {
        alert("Please enter a valid 6-digit pincode.");
        event.preventDefault();
        return false;
    }

    // You can add more specific validations based on your requirements

    return true; // Submit the form if all validations pass
});
</script>

        <div id="modal22" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <a class="close" data-dismiss="modal">x</a>
                        <center><h3><b>Wholesaler signup</b></h3></center>
                    </div>
                    <div class="modal-body">
                        <form id="wsignup" name="wsignup" method="post" enctype="multipart/form-data">
                                <div class="form-group" style="margin-left: 77px;">
                                    <input type="text" name="ownername" placeholder="Owner Name" style="height: 40px;width:400px" required>

                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Gender<input type="radio" id="wgender" name="wgender" style="margin-left: 20px;" value="Male">
                                    Male<input type="radio" id="ugender" name="wgender" style="margin-left: 20px;" value="Female">
                                    Female
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="email" id="wemail" name="wemail" placeholder="Emailid" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="date" id="wdob" name="wdob" placeholder="DOB" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="tel" id="wphno" name="wphno" pattern="[0-9]{10}" placeholder="phone number" style="height: 40px; width: 400px;" required>

                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Upload Your Photo<input type="file" name="wphoto" id="wphoto" style="margin-top: 10px;" required>    
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" id="shopname" name="shopname" placeholder="Shopname" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Shop licence<input type="file" name="licence" id="licence" style="margin-top: 10px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Shop Image<input type="file" name="shopimage" id="shopimage" style="margin-top: 10px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    Aadhaar card<input type="file" name="aadhaar" id="aadhaar" style="margin-top: 10px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wdoor" id="wdoor" placeholder="Door Number" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wstreet" id="wstreet" placeholder="street" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wcity" id="wcity" placeholder="City" style="height: 40px;width: 400px;" required>  
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wdistrict" id="wdistrict" placeholder="District" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wstate" id="wstate" placeholder="State" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="text" name="wpincode" id="wpincode" placeholder="Enter 6 digit pincode" pattern="[0-9]{6}"  maxlength="6" minlength="6" style="height: 40px;width: 400px;" required>
                                </div>
                                <div class="form-group" style="margin-left: 80px;">
                                    <input type="submit" class="btn btn-success" name="wsubmit" value="Register" style="width:30%;width: 400px;" required>
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
            <h1>Kids Section</h1>
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
                                <p style="font-size:30px;">Welcome!!</p>
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