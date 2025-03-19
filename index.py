#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
form = cgi.FieldStorage()
ID=form.getvalue("id")
x = """Select * from user where id = "%s" """%(ID)
cur.execute(x)
rec = cur.fetchall()


ID=form.getvalue("id")
y = """Select * from wholesaler where id = "%s" """%(ID)
cur.execute(y)
rec = cur.fetchall()

ID=form.getvalue("id")
y = """Select * from product where id = "%s" """%(ID)
cur.execute(y)
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
        <div>
            <div class="container">
                <div class="row" id="banner">
                    <div class="col-md-7" id="banner1">
                        <img src="assets/banner-1.jpg" alt="Banner Image" class="img-fluid" width="400px" height="500px">
                    </div>
                    <div class="col-md-5" id="banner2">
                        <h1>Fashion Story</h1>
                        <h1>Women's Lifestyle</h1>
                        <button class="btn-default" id="shopbutton"><a href="women.py" style="text-decoration: none;color: black;">Shop Collection<span class="glyphicon glyphicon-triangle-right"></span></a></button>
                    </div>
                </div>
            </div>
            <section id="collections">
                <div class="container">
                    <div class="c-2">
                        <h2>featured collection</h2>
                        <hr/>
                        <div class="c-2-image-holder"> <img class="left" src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412552/E-commerce%20landing%20page/suit-collections/collection-2-img_3x.jpg" alt=""><img class="right" src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412552/E-commerce%20landing%20page/suit-collections/collection-1-img_3x.jpg"
                            alt=""></div>
                        <p class="button"><a href="mens.py" style="text-decoration: none;">view all collections</a></p>
                    </div> <div class="c-1">
                        <div class="c-1-image-holder"> <img src="assets/mens.jpg" alt="image"> </div>
                    </div>
                </div>
            </section>
            <section id="blog">
                <div class="container">
                    <div class="blog-header">
                        <h2><b>Kids Collections</b></h2>
                    </div>
                    <div class="blog-content">
                        <div class="blog-1">
                            <div class="blog-1-image-holder"> <img src="assets/skids.jpg" alt="image"> </div>
                            <div class="blog-1-content">
                                <h3>Dress your little stars in trendy ensembles that spark imagination and spread smiles.</h3>
                                <p class="button"><a href="kids.py" id="a2"><b>Shop Collections</b></a></p>
                            </div>
                        </div>
                        <div class="blog-2">
                            <div class="blog-2-image-holder"> <img src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412543/E-commerce%20landing%20page/blog/blog-1-img_3x.jpg" alt="image"> </div>
                            <div class="blog-2-content">
                                <h3>Vibrant colors , Fun patterns , Practical features</h3>
                                <p class="button"><a href="kids.py" id="a2"><b>shop Collections</b></a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
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
    
</body>
</html>
<script>
    
    document.getElementById('signup').addEventListener('submit', function (event) {
        if (!useraccount()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    function useraccount() {
        var username = document.getElementById('username').value;
        var ugender = document.querySelector('input[name="ugender"]:checked');
        var uemail = document.getElementById('uemail').value;
        var udob = document.getElementById('udob').value;
        var upassword = document.getElementById('upassword').value;
        var ucpassword = document.getElementById('ucpassword').value;
        var uphno = document.getElementById('uphno').value;
        var udoor = document.getElementById('udoor').value;
        var ustreet = document.getElementById('ustreet').value;
        var ucity = document.getElementById('ucity').value;
        var udistrict = document.getElementById('udistrict').value;
        var ustate = document.getElementById('ustate').value;
        var upincode = document.getElementById('upincode').value;

        // Basic required field validation
        if (!username || !ugender || !uemail || !udob || !upassword || !ucpassword || !uphno || !udoor || !ustreet || !ucity || !udistrict || !ustate || !upincode) {
            alert('Please fill in all required fields.');
            return false;
        }

        // Validate email format
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(uemail)) {
            alert('Please enter a valid email address.');
            return false;
        }

        // Validate password match
        if (upassword !== ucpassword) {
            alert('Passwords do not match. Please enter matching passwords.');
            return false;
        }
        var pincodeRegex = /^\d{6}$/;
        if (!pincodeRegex.test(upincode)) {
            alert('Please enter a 6-digit pincode.');
            return false;
        }
        var phoneRegex = /^\d{10}$/;
        if (!phoneRegex.test(uphno)) {
            alert('Please enter a 10-digit phone number.');
            return false;
        }
        // Additional validation can be added based on specific requirements

        // If all validations pass, you can submit the form
        alert('Form submitted successfully!');
        return true;
    }
    
    document.getElementById('alogin').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        var username = document.getElementById('auser').value;
        var password = document.getElementById('apass').value;

        // Check if the provided username and password match the admin credentials
        if (username.toLowerCase() === 'admin' && password === 'ad123') {
            window.location.href = 'adminhome.py'; // Redirect to adminhome.py
        } else {
            alert('Invalid username or password. Please try again.');
        }
    });


    
</script>





""")



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

wsubmit=form.getvalue("wsubmit")
if wsubmit != None:
    if len(form) != 0:
            ownername=form.getvalue("ownername")
            wgender=form.getvalue("wgender")
            wemail=form.getvalue("wemail")
            wdob=form.getvalue("wdob")
            wphno=form.getvalue("wphno")
            wphoto=form["wphoto"]
            shopname=form.getvalue("shopname")
            licence=form["licence"]
            shopimage=form["shopimage"]
            aadhaarcard=form["aadhaar"]
            udoor = form.getvalue('wdoor')
            ustreet = form.getvalue('wstreet')
            ucity = form.getvalue('wcity')
            udistrict = form.getvalue('wdistrict')
            ustate = form.getvalue('wstate')
            upincode = form.getvalue('wpincode')

            if wphoto.filename and licence.filename and shopimage.filename and aadhaarcard.filename:
                    fn1 = os.path.basename(wphoto.filename)
                    open("dbmedia/" + fn1, "wb").write(wphoto.file.read())
                    fn2 = os.path.basename(licence.filename)
                    open("dbmedia/" + fn2, "wb").write(licence.file.read())
                    fn3 = os.path.basename(shopimage.filename)
                    open("dbmedia/" + fn3, "wb").write(shopimage.file.read())
                    fn4 = os.path.basename(aadhaarcard.filename)
                    open("dbmedia/" + fn4, "wb").write(aadhaarcard.file.read())
                    q="""insert into wholesaler(ownername,gender,email,dob,phno,photo,shopname,shoplicence,shopimage,aadhaarcard,door,street,city,district,state,pincode)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(ownername,wgender,wemail,wdob,wphno,fn1,shopname,fn2,fn3,fn4,udoor,ustreet,ucity,udistrict,ustate,upincode)
                    cur.execute(q)
                    con.commit()
                    print("""
                                        <script>
                                            alert("Registered successfully!!")
                                        </script>
                                """)


ulsubmit=form.getvalue("ulsubmit")
if ulsubmit != None:
    uuser = form.getvalue("user")
    upass = form.getvalue("pass")
    q = """select id from user where  username = '%s' and password = '%s' """ % (uuser, upass)
    cur.execute(q)
    rec1 = cur.fetchone()
    print("""
         <script>
            alert("Login successfully");
              location.href="userhome.py?id=%s";
         </script>
    """ % (rec1[0]))

wlsubmit=form.getvalue("wlsubmit")
if wlsubmit != None:
    wuser = form.getvalue("wuser")
    wpass = form.getvalue("wpass")
    q = """select id from wholesaler where  ownername = '%s' and password = '%s' """ % (wuser, wpass)
    cur.execute(q)
    rec2 = cur.fetchone()
    print("""
         <script>
            alert("Login successfully");
              location.href="wholehome.py?id=%s";
         </script>
    """ % (rec2[0]))

esubmit=form.getvalue("esubmit")
if esubmit != None:
    euser = form.getvalue("euser")
    epass = form.getvalue("epass")
    q = """select id from employee where  employeename = '%s' and password = '%s' """ % (euser, epass)
    cur.execute(q)
    rec2 = cur.fetchone()
    print("""
         <script>
            alert("Login successfully");
              location.href="employeehome.py?id=%s";
         </script>
    """ % (rec2[0]))

esubmit1=form.getvalue("esubmit2")
if esubmit1 != None:
    euser1 = form.getvalue("euser2")
    epass1 = form.getvalue("epass2")
    q4 = """select id from employee where  employeename = '%s' and password = '%s' """ % (euser1, epass1)
    cur.execute(q4)
    rec4 = cur.fetchone()
    print("""
         <script>
            alert("Login successfully");
              location.href="deliveryemphome.py?id=%s";
         </script>
    """ % (rec4[0]))













