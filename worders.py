#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
x = """Select * from wholesaler where id = "%s" """ % (ID)
cur.execute(x)
recc = cur.fetchall()

q = """Select* from wholeorders"""
cur.execute(q)
rec1 = cur.fetchall()

q = """SELECT wholesaler.ownername,wholesaler.door,wholesaler.street,wholesaler.city,wholesaler.district,wholesaler.state,wholesaler.pincode,wholesaler.phno,wholesaler.shopname,wholeorders.productname,wholeorders.quantity,wholeorders.size,wholeorders.price,wholeorders.totalprice,wholeorders.status,wholeorders.id,wholeorders.receive FROM wholeorders INNER JOIN wholesaler ON wholeorders.userid = wholesaler.id where wholeorders.userid="%s" AND wholeorders.status="Confirm" """ % ID
cur.execute(q)
rec = cur.fetchall()

q3 = """SELECT SUM(totalprice) FROM wholeorders WHERE userid="%s" and status = "Confirm" """ % ID
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
q2 = """Select ownername from wholesaler where id = "%s" """ % ID
cur.execute(q2)
name = cur.fetchone()
q4 = """Select door from wholesaler where id = "%s" """ % ID
cur.execute(q4)
address = cur.fetchone()
q6 = """Select street from wholesaler where id = "%s" """ % ID
cur.execute(q6)
address1 = cur.fetchone()
q7 = """Select city from wholesaler where id = "%s" """ % ID
cur.execute(q7)
address2 = cur.fetchone()
q8 = """Select district from wholesaler where id = "%s" """ % ID
cur.execute(q8)
address3 = cur.fetchone()
q9 = """Select state from wholesaler where id = "%s" """ % ID
cur.execute(q9)
address4 = cur.fetchone()
q10 = """Select pincode from wholesaler where id = "%s" """ % ID
cur.execute(q10)
address5 = cur.fetchone()

q5 = """Select phno from wholesaler where id = "%s" """ % ID
cur.execute(q5)
phno = cur.fetchone()
print("""   
        <div class="container-fluid">
            <h1><b>Your Orders</b></h1>
            <hr>
            <br>
            <br>
            <div class="row">
            <div class="col-md-2"></div>
        <div class="col-md-8">
        <div class="container mt-3">
            <div class="row  text-capitalize color">
                <div class="col-lg-12 text--container mt-4">

                </div>
    """)
print("""
                <center><h2 class="mt-4"><b>Ordered Products</b></h2></center>
                <div class="col-md-12">

                    <table class="table text-center">
                        <tr>
                            <th>ProductName</th>
                            <th>Quantity</th>
                            <th>Size</th>
                            <th>Price</th>
                            <th>Totalprice</th>
                        </tr>
""")
for i in rec:
    if i[16]!="Product Received":
        print("""
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>
                            <form method="post" enctype="multipart/form-data">
                                <input type="hidden" name="oid" value="%s">
                                <input type="submit" class="btn btn-primary" value="Product Received" name="receive">
                            </form>    
                            </td>
                        </tr>
                        """ % (i[9], i[10], i[11], i[12], i[13], i[15]))
print("""
                <div class="container">
                    <hr>
                </div>
                <div class="col-md-6"></div>
                <div class="col-md-6 mb-4">
                    <table class="table text-center">

                        <tr>
                            <th>Delivered to: </th>
                            <td>%s,%s,%s,%s,%s,%s</td>
                        </tr>
                        <tr>
                            <th>Phone number: </th>
                            <td>%s</td>
                        </tr>
                    </table>
                </div>
            </div>
            </div>
        <div class="col-md-2"></div><br><br>
        </div><br><br>
          """ % (address[0], address1[0], address2[0], address3[0], address4[0], address5[0], phno[0]))

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
receive = form.getvalue("receive")
oid = form.getvalue("oid")

if receive != None:
    q = """Update wholeorders set receive="%s" where id="%s" """ % (receive, oid)
    cur.execute(q)
    con.commit()
    print("""
        <script>
            alert("Product received");
        </script>  
    """)



