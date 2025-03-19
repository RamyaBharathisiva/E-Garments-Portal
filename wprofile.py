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
    <style>
        #text{
    font-size: 75px;
    color:white;
    margin-left: 0px;
    padding-top: 50px;

} 
        #front {
            background-image: url(assets/u2.jpg);
            background-repeat: no-repeat;
            background-size: cover;
            height: 600px;
            position: relative;
            overflow: hidden;
        }
        table{
            margin-top: 20px;
        }
        th{
            font-size: 20px;
            /* padding-left: 50px; */
            /* margin-left: 20px; */
        }
        #add{
            margin-left: 180px;
        }
        td{

            font-size: 30px;
            /* margin-left: 40px; */
        }
        #form{
            /* border: 2px solid black; */
            border-radius: 20px;
            box-shadow: 0px 20px 40px -10px rgb(187, 115, 115);
            background-color: white;
            padding-top: 10px;
            padding-left: 90px;
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
  <a href="wwomen.py?id=%s" style="margin-top: 10px;"><b>Women</b></a>
  <a href="wmen.py?id=%s" style="margin-top: 20px;"><b>Men</b></a>
  <a href="wkids.py?id=%s" style="margin-top: 20px;"><b>Kids</b></a>
  <a href="wdesign.py?id=%s" style="margin-top: 20px;color:rgb(231, 183, 120);"><b>Design</b></a>
  <a href="woffers.py?id=%s" style="margin-top: 20px;color:rgb(231, 183, 120);"><b>Offers</b></a>
  <a href="wprofile.py?id=%s" style="margin-top: 20px;"><b>Profile</b></a>
  <a href="worders.py?id=%s" style="margin-top: 20px;"><b>Orders</b></a>
  
  <a href="wfeedback.py?id=%s" style="margin-top: 20px;"><b>Feedback</b></a>
</div>""" % (ID, ID, ID, ID, ID, ID, ID, ID))

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
for i in rec:
    print("""
        <div class="tabular--wrapper">
            <p class="main--title" style="font-size:50px;">
               <b> Profile</b>
            </p>
               <div class="row text-center">
                    <div class="col-md-3"></div>

                    <div class="col-md-6 mt-4">
                        <div class="form--container">
                            <form  method="post" enctype="multipart/form-data">
                                <table class="table add">
                                    <tr>
                                        <th><input type="text" name="username" value='%s' readonly class="text-capitalize form-control text-center mt-4" style="font-size:30px;color:white;background-color:black;">
                                        </th>

                                    </tr>
                                    <tr>
                                        <th>Shop Name</th>
                                        <td>
                                        <input type="text" name="shop" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Door No</th>
                                        <td><input type="number" name="door" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Street</th>
                                        <td>
                                        <input type="text" name="street" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>city</th>
                                        <td>
                                        <input type="text" name="city" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>District</th>
                                        <td>
                                        <input type="text" name="district" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>State</th>
                                        <td>
                                        <input type="text" name="state" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Pincode</th>
                                        <td><input type="number" name="pincode" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Mobile Number</th>
                                        <td>
                                        <input type="number" name="ephno" value='%s' class="form-control"></td>
                                        
                                    </tr>
                                </table>
                                <center><input type="submit" name="update" value="Update" class="btn btn-md btn-primary" style="font-size:30px;"></center>
                            </form>
                        </div>
                    </div>
                    <div class="col-md-3"></div>
        """ % (i[1], i[7],i[11], i[12], i[13], i[14], i[15], i[16], i[5]))
update = form.getvalue("update")
username = form.getvalue("username")
door = form.getvalue("door")
street = form.getvalue("street")
city = form.getvalue("city")
district = form.getvalue("district")
state = form.getvalue("state")
pincode = form.getvalue("pincode")
phno = form.getvalue("ephno")
shop=form.getvalue("shop")


if update != None:
        q = """Update wholesaler set door="%s", street="%s",city="%s",district="%s",state="%s",pincode="%s", shopname="%s",phno="%s" where id="%s" """ % (
        door, street, city, district, state, pincode, shop,phno, ID)
        cur.execute(q)
        con.commit()
        print("""
                <script>
                    alert("Updated Successfully!!");
                </script>
            """)