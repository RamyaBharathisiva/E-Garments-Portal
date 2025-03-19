#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from product where category = "kids" """
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
</div>"""%(ID,ID,ID,ID,ID,ID,ID,ID))

print("""
<div id="main">
        <nav class="navbar navbar" style="font-size: 10px;box-shadow: 0px 5px 20px -10px rgb(0, 0, 0);">
            <div class="container-fluid">
                    <span style="font-size:40px;cursor:pointer;" onclick="openNav()" id="open">&#9776;</span>
                    <a href="wholehome.py" class="navbar-brand mx-auto">
                        <img src="assets/Logo2.png" id="logo" alt="logo" class="navbar-brand">
                    </a>
                    <div class="navbar-right">
                        <a href="home.py" id="log"><b>Logout</b></a>
                    </div>
            </div>
        </nav>
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
                            <button type="button" class="btn" data-toggle="modal" data-target="#myModal-%s" style="background-color: rgb(188, 37, 87);color:white;">
                                <b>BUY NOW</b>
                              </button>
                </div>""" % (fn, i[2], i[4], i[9],i[0]))
    print("""    <div id="myModal-%s" class="modal fade" role="dialog">
                    <div class="modal-dialog modal-lg">
                        <form action="" name="order" id="login">
                        <div class="modal-content">
                            <div class="modal-header" style="border: none;">
                                <a class="close" data-dismiss="modal"><b>x</b></a>
                            </div>
                            <div class="modal-body" style="margin-top:20px;">
                                    <div class="col-md-4">
                                        <img class="dress-card-img-top" src="%s" alt="img">
                                    </div>
                                    <div class="col-md-1"></div>
                                    <div class="col-md-5">
                                    <h4 class="dress-card-title">%s</h4>
                                        <p class="dress-card-para"><b>%s</b></p>
                                    <div class="form-group">
                                                <select name="size" id="" style="font-size: 20px;" required>
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
                                                <select name="quantity" id="quantity%s" style="font-size: 20px;" onchange="myfun()%s" required>
                                                    <option value="select" selected disabled>Quantity</option>
                                                    <option value="1">1</option>
                                                    <option value="2">2</option>
                                                    <option value="3">3</option>
                                                    <option value="4">4</option>
                                                </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="price">Price</label>
                                        <input type="number" id="price%s" name="price" value="%s"  class="form-control" readonly>
                                    </div>
                                    <div class="form-group">
                                        <label for="price">Total Price</label>
                                        <input type="text" id="totalprice%s" name="totalprice" class="form-control" readonly>
                                    </div>
                                    <div class="form-group">
                                        <b>Payment method:</b><br>         
                                        <input type="radio" name="pay" id="radio1" class="form-check-input" value="credit or debit card"  checked>Credit or Debit card<label class="form-check-label" for="radio1"></label>
                                    </div>
                                    <div class="form-group">
                                                    <b>Enter Card Number:</b>
                                                    <input type="number" name="card" class="form-control" required>
                                    </div>
                                    <div class="form-group">
                                                    <b>Expiry Date:</b>
                                                    <input type="date" name="edate" class="form-control" required>
                                    </div>
                                    <div class="form-group">
                                                <input type="hidden" name="proname" value="%s">
                                                <input type="hidden" name="proid" value="%s">
                                                <input type="hidden" name="category" value="%s">
                                                
                                                <input type="submit" class="btn" name="placeorder" value="Place Order" style="background-color:rgb(28, 108, 80);border: none;color:rgb(255, 253, 253);font-size: 30px;margin-top: 40px;border-radius: 2px;">
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                            
                            </div>
                        </form>
                        </div>
                    </div>
                </div>


""" % (i[0],fn, i[2], i[4], i[0],i[0],i[0],i[9],i[2],i[1],i[7],i[9]))
print("""
    
</body>
</html> 
  """)

order = form.getvalue("placeorder")
proname = form.getvalue("proname")
proid = form.getvalue("proid")
category=form.getvalue("category")
quan = form.getvalue("quantity")
size = form.getvalue("size")
prize = form.getvalue("totalprice")
card = form.getvalue("pay")
cardno = form.getvalue("card")
exdate = form.getvalue("edate")

if order != None:
    if len(form) != 0:
        q="""insert into wholeorders(productid,productname,category,quantity,size,price,card,cardno,expirydate)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(proname,proid,category,quan,size,prize,card,cardno,exdate)
        cur.execute(q)
        con.commit()
        print("""
                    <script>
                        alert("Your order placed");
                    </script>
                """)


