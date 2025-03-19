#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()

q = """SELECT orders.id,user.username,user.door,user.street,user.city,user.district,user.state,user.pincode,user.phno,orders.productname,orders.quantity,orders.size,orders.price,orders.totalprice,orders.card,orders.cardno,orders.expirydate,orders.status,orders.category,orders.ordertime,orders.action FROM orders INNER JOIN user ON orders.userid = user.id where orders.status ="Confirm" and orders.action!='Product Delivered'"""
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
    <link rel="stylesheet" type="text/css" href="./assets/css/homepage.css" /> 
    <style>
        *{
            margin: 0;
            padding:0;
            box-sizing: border-box;
            font-family: sans-serif;
        }
        body{
           
        }
        .container{
            height: 100%;
            width:250px;
            position: absolute;
            background: #161616;
            z-index:1;
            transition: 0.5s ease;
            transform: translateX(-250px);
        }
        .container #head{
            color:antiquewhite;
            font-size: 20px;
            font-weight: bold;
            padding: 30px;
            text-transform: uppercase;
            letter-spacing: 5px;
            background-image: linear-gradient(30deg,#df0155,#ed4901);
            margin-left: 20px;

        }
        #head:hover{
            color:rgb(37, 24, 24);
        }
        ol{
            width:100%;
            list-style:none;
            margin-top:40px;
        }
        ol li{
            display: block;
            width: 100%;
        }
        ol li a{
            color:#fbfdce;
            padding: 15px 10px;
            text-decoration: none;
            display: block;
            font-size: 20px;
            letter-spacing: 1px;
            position: relative;
            transition: 0.3s;
            overflow: hidden;
            text-transform: capitalize;           
        }
        ol li a i{
            width:70px;
            font-size: 25px;
            text-align: center;
            padding-left: 30px;

        }
        ol li:hover a{
            background: #030303;
            color: #00eaff;
            letter-spacing: 5px;
            text-decoration: none;
        }
        #whole{
            margin-top: 40px;
        }
        #side{
            margin-top: 20px;
        }
        #check{
            -webkit-appearance: none;
            visibility: hidden;
            display: none;
        }
        span{
            position: absolute;
            right:-40px;
            top:30px;
            font-size: 25px;
            border-radius:3px;
            color:#fff;
            padding:3px 8px;
            cursor:pointer;
            background: #850000;
        }
        #bars{
            background: red;
        }
        #check:checked ~ .container{
            transform: translateX(0);
        }
        #check:checked ~ .container #bars{
            display: none;
        }
        #checked:checked ~ section{
            transform: scale(1.2);
            filter:brightness(20%);
        }
        #brand{
            color:white;
        }
        .navbar-inverse #brand:hover{
            color:red;
            word-spacing:2px;
        }
        .navbar-inverse #log{
            color:white;  
        }
        .navbar-inverse #log:hover{
            color:red;
            letter-spacing:1px;
        }
        .section{
            width: 100%;
            padding: 20px;
            min-width: 100vh;

        }
        #profile{
            size:200px;
        }
        .profile{
            /* border:2px solid black; */
            border-radius: 20px;
            margin-top: 90px;
            background-color:whitesmoke;
            box-shadow: 0px 20px 40px -10px rgb(0, 0, 0);
        }

    </style>
</head>
<body>
    <div class="wrapper">
        <nav class="navbar navbar-inverse" style="font-size: 10px;">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynav">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a href="homepage.html" class="navbar-brand" id="brand">Style Sphere</a>
                </div>
                <div class="collapse navbar-collapse" id="mynav">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="home.py" id="log" style="font-size:20px;">Logout</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <input type="checkbox" name="" id="check">
        <div class="container" style="margin-top: -20px;">
            <label for="check">
                <span class="fas fa-times" id="times"></span>
                <span class="fas fa-bars" id="bars"></span>        
            </label>
            <div></div>
            <div class="head"><a href="deliveryemphome.py" style="text-decoration: none;" id="head">Employee</a></div>
            <ol>
                        <li><a href="deliemporder.py">User Orders</a></li>
                        <li><a href="deliemporderwhole.py">Wholesaler Orders</a></li>
                        

            </ol>
        </div>
        </div>
    <div class="main--content">
        <div class="main--title">
                <div class="col-md-10">
                    <h1><b>User Orders</b></h1>
                </div>
            </div>
            <div class="table--wrapper">
                <div class="table--container">
                    <div class="col-md-12">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Order Id</th>
                                    <th>Product name</th>
                                    <th>Category</th>
                                    <th>Quantity</th>
                                    <th>Size</th>
                                    <th>Price</th>
                                    <th>Totalprice</th>
                                    <th>Payment Method</th>
                                    <th>Card Number</th>
                                    <th>Expiry Date</th>
                                    <th>Userid</th>
                                    <th>Phone number</th>
                                    <th>door</th>
                                    <th>street</th>
                                    <th>city</th>
                                    <th>district</th>
                                    <th>state</th>
                                    <th>pincode</th>
                                    <th>Ordered time</th>
                                    <th>Action</th>   
                                </tr>
                            </thead>
""")
for i in rec:

    print("""

                               <tbody>
                                <tr>
                                <form method="post">
                                    <td>%s</td>     
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <input type="hidden" name="orderid" value="%s">
                                    <td><input type="submit" name="deliver" class="btn btn-success" value="Product Delivered"></td>
                                </form>
                                </tr>
    """ % (i[0], i[9], i[18], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[1], i[8], i[2], i[3], i[4], i[5], i[6],
           i[7], i[19], i[0]))
print("""
    </div>
</body>
</html>""")


form = cgi.FieldStorage()
confirm = form.getvalue("deliver")
orderid = form.getvalue("orderid")

if orderid != None:
        if confirm != None:
                q = """Update orders set action = "%s" where id="%s" """ % (confirm, orderid)
                cur.execute(q)
                con.commit()
                print("""
                <script>
                    alert("Product Delivered");
                </script>
                """)
    
    
    
    
    
    
    
    
    


