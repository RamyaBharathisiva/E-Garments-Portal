#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()


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
            font-size: 30px;
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
            margin-top: 10px;
        }
        input{
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
            <div class="head"><a href="adminhome.py" style="text-decoration: none;" id="head">Admin</a></div>
            <ol>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="whole">Wholesaler <span class="caret" style="color: white;"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="newwholesaler.py">New User</a></li>
                        <li><a href="existingwholesaler.py">Existing User</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User</a>
                    <ul class="dropdown-menu">
                        <li><a href="newuser.py">New User</a></li>
                        <li><a href="existinguser.py">Existing User</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Employee</a>
                    <ul class="dropdown-menu">
                        <li><a href="addemployee.py">Add Employee</a></li>
                        <li><a href="existingemployee.py">Existing Employee</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Product<span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="newproduct.py">New Product</a></li>
                        <li><a href="existingproduct.py">Existing Product</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Offers</a>
                    <ul class="dropdown-menu">
                         <li><a href="addoffers.py">Add Offers</a></li>
                         <li><a href="existingoffers.py">Existing Offers</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="order.py" id="side">New Orders</a></li>
                         <li><a href="exorder.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Wholesaler Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="newwholeorder.py" id="side">New Orders</a></li>
                         <li><a href="exwholeorders.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">User Design Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="userdesign.py" id="side">New Orders</a></li>
                         <li><a href="exuserdesign.py">Existing Orders</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="side">Wholesaler Design Orders</a>
                    <ul class="dropdown-menu">
                         <li><a href="wholedesign.py" id="side">New Orders</a></li>
                         <li><a href="exwholedesign.py">Existing Orders</a></li>
                    </ul>
                </li>
                
            </ol>
        </div>
        </div>
    <div class="main--content">
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4 profile" >
                <img src="assets/icon.jpg" alt="profile" height="350px" width="350px" style="margin-left: 70px; margin-top: 20px;"><br>
                <!-- <b style="font-size: 30px;">Profile</b><br> -->
                <b style="font-size: 40px;margin-left: 80px;">Welcome Admin!</b>
            </div>
            <div class="col-md-4"></div>
        </div>
    </div>
</body>
</html>""")
