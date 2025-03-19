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
</div>"""%(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))

print("""<div id="main">
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
    </nav>""" % (ID, ID, ID,ID))
print("""
    <div>
        <div class="container">
            <div class="row" id="banner">
                
                <div class="col-md-7" id="banner1">
                    <img src="assets/banner-1.jpg" alt="Banner Image" class="img-fluid" width="400px" height="500px">
                </div>
    
                
                <div class="col-md-5" id="banner2">
                    <h1>Fashion Story</h1>
                    <h1>Women's Lifestyle</h1>
                    <button class="btn-default" id="shopbutton"><a href="uwomen.py?id=%s" style="text-decoration: none;color: black;">Shop Collection<span class="glyphicon glyphicon-triangle-right"></span></a></button>
                </div>
            </div>
        </div>""")
print("""
        <section id="collections">
            <div class="container">
                <div class="c-2">
                    <h2>featured collection</h2>
                    <hr/>
                    <div class="c-2-image-holder"> <img class="left" src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412552/E-commerce%20landing%20page/suit-collections/collection-2-img_3x.jpg" alt=""><img class="right" src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412552/E-commerce%20landing%20page/suit-collections/collection-1-img_3x.jpg"
                        alt=""></div>
                    <p class="button"><a href="umen.py?id=%s" style="text-decoration: none;">view all collections</a></p>

                </div> <div class="c-1">
                    <div class="c-1-image-holder"> <img src="assets/mens.jpg" alt="image"> </div>
                </div>
            </div>
        </section>""")
print("""
        
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
                           
                            <p class="button"><a href="ukids.py?id=%s" id="a2"><b>Shop Collections</b></a></p>
                        </div>
                    </div>
                    <div class="blog-2">
                        <div class="blog-2-image-holder"> <img src="https://res.cloudinary.com/de8cuyd0n/image/upload/v1520412543/E-commerce%20landing%20page/blog/blog-1-img_3x.jpg" alt="image"> </div>
                        <div class="blog-2-content">
                            
                            <h3>Vibrant colors , Fun patterns , Practical features</h3>
                            
                            <p class="button"><a href="ukids.py?id=%s" id="a2"><b>shop Collections</b></a></p>
                        </div>
                    </div>
                </div>
            </div>
        </section>""")
print("""
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
  
</div>

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
   
</body>
</html> 
""")