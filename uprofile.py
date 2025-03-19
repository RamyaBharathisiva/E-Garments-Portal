#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
x = """Select * from user where id = "%s" """ %(ID)
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
                            <li><a href="uprofile.py?id=%s"><b><i class="fas fa-edit"></i> Edit Profile</b></a></li>
                            <li><a href="uorders.py?id=%s"><b><i class="fa-solid fa-cart-shopping"></i> Orders</b></a></li>
                            <li><a href="home.py?id=%s"><b><i class="fa fa-sign-out" style="font-size:24px"></i> Logout </b></a></li>

                        </ul>
                </div>
        </div>
    </nav>"""%(ID,ID,ID))
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
        """%(i[1],i[7],i[8],i[9],i[10],i[11],i[12],i[6]))
update = form.getvalue("update")
username=form.getvalue("username")
door=form.getvalue("door")
street=form.getvalue("street")
city=form.getvalue("city")
district=form.getvalue("district")
state=form.getvalue("state")
pincode=form.getvalue("pincode")
phno = form.getvalue("ephno")

if update != None:
    if len(form)!=0:
            q = """Update user set door="%s", street="%s",city="%s",district="%s",state="%s",pincode="%s", phno="%s" where id='%s' """ %(door,street,city,district,state,pincode,phno,ID)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                    alert("Updated Successfully!!");
                </script>    
            """)