#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from product where wholesaleroffer>0 """
cur.execute(q)
rec = cur.fetchall()

form=cgi.FieldStorage()
ID=form.getvalue("id")
y = """Select * from wholesaler where id = "%s" """%(ID)
cur.execute(y)
recc = cur.fetchall()
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

    </style>
</head>
<body>
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
   <a href="userlatest.py?id=%s" style="margin-top: 30px;color:rgb(231, 183, 120);"><b>Latest Launch</b></a>
   <div class="dropdown">
        <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Women</b><span class="caret"></span></a>
            <ul class="dropdown-menu">
                  <li><a href="wholekurta.py?id=%s">kurtas kurtis</a></li>
                  <li><a href="whole wbottom.py?id=%s">Bottom Wear</a></li>
                  <li><a href="wholeparty.py?id=%s">Party Dresses</a></li>
                  <li><a href="whole wsports.py?id=%s">Sports Wear</a></li>
                  <li><a href="whole wwinter.py?id=%s">Winter Wear</a></li>
            </ul>
   </div>
   <div class="dropdown">
            <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Men</b><span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="whole mtop.py?id=%s">Top Wear</a></li>
                  <li><a href="whole mbottom.py?id=%s">Bottom Wear</a></li>
                  <li><a href="whole msports.py?id=%s">Sports Wear</a></li>
                  <li><a href="whole mwinter.py?id=%s">Winter Wear</a></li>
                </ul>
   </div>  
   <div class="dropdown">                
            <a href="#" data-toggle="dropdown" class="dropdown-toggle" style="margin-top: 30px;"><b>Kids</b><span class="caret"></span></a>
            <ul class="dropdown-menu">
                 <li><a href="whole kids1.py?id=%s">Boys clothing</a></li>
                 <li><a href="whole kids2.py?id=%s">Girls Clothing</a></li>
                 <li><a href="whole kids3.py?id=%s">Baby Boys Clothing</a></li>
                 <li><a href="whole kids4.py?id=%s">Baby Girls Clothing</a></li>
            </ul>
   </div>         
   <a href="wdesign.py?id=%s" style="margin-top: 30px;color:rgb(231, 183, 120);"><b>Design</b></a>
   <a href="woffers.py?id=%s" style="margin-top: 30px;"><b>Offers</b></a>
   <a href="wfeedback.py?id=%s" style="margin-top: 30px;"><b>Feedback</b></a>
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
                            <li><a href="wprofile.py?id=%s"><b><i class="fas fa-edit"></i> Edit Profile</b></a></li>
                            <li><a href="worders.py?id=%s"><b><i class="fa-solid fa-cart-shopping"></i> Orders</b></a></li>
                            <li><a href="wdesignorders.py?id=%s"><b><i class="fa-solid fa-cart-shopping"></i> Design Orders</b></a></li>
                            <li><a href="home.py?id=%s"><b><i class="fa fa-sign-out" style="font-size:24px"></i> Logout </b></a></li>

                        </ul>
                </div>
        </div>
    </nav>"""%(ID,ID,ID,ID))
print("""
        <div class="container-fluid">
            <p style="font-size: 40px;color:rgb(114, 4, 63);"><b>OFFERS</b></p>
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
                            <p class="dress-card-para"><span class="dress-card-price"><b><strike>Rs.%s</strike>Rs.%s <b>&ensp;</span></p>
                            <button type="button" class="btn" data-toggle="modal" data-target="#myModal-%s" style="background-color: rgb(188, 37, 87);color:white;">
                                <b>BUY NOW</b>
                              </button>
                </div>""" % (fn, i[2], i[4], i[9],i[10],i[1]))
    print("""    <div id="myModal-%s" class="modal fade" role="dialog">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header" style="border:none;">
                                <a class="close" data-dismiss="modal"><b>x</b></a>
                            </div>
                            <div class="modal-body">
                                <div class="row">
                                    <div class="col-md-6">
                                        <img class="dress-card-img-top" src="%s" alt="img">
                                    </div>
                                    <div class="col-md-6" style="margin-top:25px;padding-left: 60px;">
                                        <h4 class="dress-card-title">%s</h4>
                                        <p class="dress-card-para" style="color: rgb(218, 27, 59);"><b>%s</b></p>
                                        <form action="" name="order" id="login">
                                            <div class="form-group">
                                                <select name="size" id="" style="font-size: 20px;">
                                                    <option value="select" selected disabled>select Size</option>
                                                    <option value="s">S</option>
                                                    <option value="m">M</option>
                                                    <option value="l">L</option>
                                                    <option value="xl">XL</option>
                                                    <option value="xxl">XXL</option>
                                                    <option value="xxxl">XXXL</option>
                                                </select>
                                            </div>  
                                            <div class="form-group">
                                                <select name="quanity" id="" style="font-size: 20px;">
                                                    <option value="select" selected disabled>Quantity</option>
                                                    <option value="12">12 piece</option>
                                                    <option value="24">24 piece</option>
                                                    <option value="48">48 piece</option>
                                                    <option value="100">100 piece</option>
                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <p class="dress-card-para"><span class="dress-card-price"><b><strike>Rs.%s</strike>Rs.%s <b> &ensp;</span></p>
                                            </div>
                                            <div class="form-group">
                                                <input type="submit" class="btn" name="placeorder" value="Place Order" style="background-color:rgb(28, 108, 80);border: none;color:rgb(255, 253, 253);font-size: 20px;margin-top: 40px;border-radius: 2px;">
                                            </div>
                                        </form>
                                    </div>       
                                </div>
                            </div>
                            <div class="modal-footer"style="border:none;"></div>
                        </div>
                    </div>
                </div>

""" % (i[1],fn, i[2], i[4], i[9],i[10]))
print("""
    
</body>
</html> 

  """)

