#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """Select * from product where status = "approved" """
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
            font-size: 30px;
            font-weight: bold;
            padding: 20px;
            text-transform: uppercase;
            letter-spacing: 3px;
            background-image: linear-gradient(30deg,#df0155,#ed4901);
            top:0;
            margin-left: 0;

        }
        #head:hover{
            color:rgb(37, 24, 24);
        }
        ol{
            width:100%;
            list-style:none;
            margin-top: 30px;
        }
        ol li{
            display: block;
            width: 100%;
            margin-top: 20px;
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
            background: #000;
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
        #log{
            font-size:20px;
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
            margin-top: 50px;
            background-color:whitesmoke;
            box-shadow: 0px 20px 40px -10px rgb(0, 0, 0);
        }
        table{
            margin-top: 10px;
        }
        th{
            font-size: 15px;
        }
        #add{
            margin-left: 120px;
        }
        td{
            height: 50px;
            width: 50px;
            font-size: 20px;
        }
        #form{
            /* border: 2px solid black; */
            border-radius: 20px;
            box-shadow: 0px 20px 40px -10px rgb(187, 115, 115);

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
                        <li><a href="./homepage.html" id="log">Logout</a></li>
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
            <div class="head"><a href="employeehome.py" style="text-decoration: none;" id="head">Employee</a></div>
            <ol>
                <li><a href="addproduct.py">Add Product</a></li>
                <li><a href="eexistingproduct.py">Existing product</a></li>
            </ol>


            </div>
        </div>    
        <div class="main--content" style="margin-left: 100px;">
        <div class="tabular-wrapper">
            <h3 class="min-title" style="font-size: 20px;"><b>Existing Product Details</b></h3>
            <div class="table-container">
                <table class="table">
                        <tr>
                            <th>id</th>
                            <th>Product id</th>
                            <th>Product Name</th>
                            <th>Product Image</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Size</th>
                            <th>Product Category</th>
                            <th>Product Price</th>
                        <tr>
    """)

for i in rec:
    fn1 = "product/" + i[3]
    print("""
                                <tr>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td><img src="%s" alt="img" width="100px" height="100px"></td>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                                            <td>%s</td>
                                </tr>
                                            
    """%(i[0],i[1],i[2],fn1,i[4],i[5],i[6],i[7],i[8]))



