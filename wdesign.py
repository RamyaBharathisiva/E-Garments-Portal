#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()

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
            height: 60px;
            width: 90px;
            font-size: 20px;
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
    <div class="row" id="front">
        <div class="col-md-6" style="height: 400px;padding: 80px;">
            <h1><b id="text">WE MAKE CLOTHS <br>THAT SUIT YOU</b></h1>
        </div>
        <div class="col-md-6" id="left">
            
        </div>
    </div>
    <div class="container-fluid">

   
    <div class="row" id="f1" style="margin-top: -150px;">
        <div class="col-md-3"></div>
        <div class="col-md-6" id="form">
            <h2 id="add"><b></b></h2>
            <form name="Designform" action="" method="post" enctype="multipart/form-data" onsubmit="">
                <table class="table">
                    <tr style="border: hidden;">
                        <th><b>Design for:</b></th>
                        <td>
                        <select name="designfor" id="" required>
                            <option value="select" selected disabled>select </option>
                            <option value="men">Men</option>
                            <option value="women">Women</option>
                            <option value="kids">Kids</option>
                        </select>
                        </td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Select Gender:</b></th>
                        <td><select name="gender" id="" required>
                            <option value="select" selected disabled>select Gender</option>
                            <option value="male">Male</option>
                            <option value="female">female</option>
                        </select>
                        </td>
                    </tr>
                    <tr style="border: hidden;">
                        <th> <b>Dress Type:</b></th>
                        <td><input type="text" name="dresstype" required></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Fabric:</b></th>
                        <td><input type="text" name="frabric" required></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Color:</b></th>
                        <td><input type="text" name="color" required></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Size:</b></th>
                        <td><select name="size" id="">
                            <option value="select" selected disabled>select Size</option>
                            <option value="s">S</option>
                            <option value="m">M</option>
                            <option value="l">L</option>
                            <option value="xl">XL</option>
                            <option value="xxl">XXL</option>
                            <option value="xxxl">XXXL</option>
                        </select></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Age:</b></th>
                        <td><input type="number" name="age" min="1" max="90"></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Reference Image:</b></th>
                        <td><input type="file" name="Referanceimage" required></td>
                    </tr>
                    <tr style="border: hidden;">
                        <th><b>Quantity:</b></th>
                        <td>
                            <select name="productquantity" id="">
                                <option value="12">12 piece</option>
                                <option value="24">24 piece</option>
                                <option value="48">48 piece</option>
                                <option value="100">100 piece</option>
                            
                            </select>
                        
                        </td>
                            
                    </tr>
                    <tr>
                        <th><b>Additional Request:</b></th>
                        <td><textarea name="request" cols="30" rows="5" required></textarea></td>
                    </tr>
                    
                    
                    <tr>
                        <th></th>
                    </tr>
                    <tr style="border: hidden;">
                        <th></th>
                        <td><input type="submit" name="submit" class="btn btn-success" value="Request for Design" style="font-size: 30px;margin-left: -50px;"></td>
                    </tr>
                </table>
            </form>
        </div>
        <div class="col-md-3"></div>
    </div>    </div>
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
</body>
</html>
""")

# submit=form.getvalue("submit")
# adrequest=form.getvalue("Additional request")
# quantity=form.getvalue("quantity")
# image=form["Referanceimage"]
# age=form.getvalue("age")
# size=form.getvalue("size")
# frabric=form.getvalue("frabric")
# dresstype=form.getvalue("dresstype")
# gender=form.getvalue("gender")
# designfor=form.getvalue("designfor")
submit=form.getvalue("submit")
if submit != None:
    if len(form) != 0:
        design=form.getvalue("designfor")
        gender=form.getvalue("gender")
        dresstype=form.getvalue("dresstype")
        frabric=form.getvalue("frabric")
        color=form.getvalue("color")
        size=form.getvalue("size")
        age=form.getvalue("age")
        Referanceimage=form["Referanceimage"]
        productquantity=form.getvalue("productquantity")
        request=form.getvalue("request")
        if Referanceimage.filename:
            fn=os.path.basename(Referanceimage.filename)
            open("design/" + fn,"wb").write(Referanceimage.file.read())
            q="""insert into wholedesign(userid,designfor,gender,dresstype,fabric,color,size,age,referenceimage,quantity,additionalrequest)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(ID,design,gender,dresstype,frabric,color,size,age,fn,productquantity,request)
            cur.execute(q)
            con.commit()
            print("""
                     <script>
                        alert("Request submitted successfully!! You Can Verify the Design Order menu whether your order is accepted or not")
                    </script>
                                            """)




