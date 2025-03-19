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
    <style>
        *{
            margin: 0;
            padding:0;
            box-sizing: border-box;
            font-family: sans-serif;
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
            margin-top:-50px;
            box-shadow: 0px 20px 40px -10px rgb(187, 115, 115);

        }
        #log{
        font-size:20px;
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
                        <li><a href="home.py" id="log">Logout</a></li>
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
            <div class="head"><a href="./employee.html" style="text-decoration: none;" id="head">Employee</a></div>
            <ol>
                <li><a href="addproduct.py">Add Product</a></li>
                <li><a href="eexistingproduct.py">Existing product</a></li>
                
            </ol>


            </div>
        """)
print("""
        <div class="container-fluid">
        <div class="main-content">
                <div class="row">
                    <div class="col-md-4"></div>
                    <div class="col-md-4" id="form" style="margin-top: 5px;padding: 20px;">
                        <h2 id="add"><b>Add Product</b></h2>
                        <form method="post" enctype="multipart/form-data">
                            <table class="table">
                                <tr style="border: hidden;">
                                    <th><b>Product ID:</b></th>
                                    <td><input type="number" name="productid"></td>
                                </tr>
                                <tr style="border: hidden;">
                                    <th> <b>Product Name:</b></th>
                                    <td><input type="text" name="productname"></td>
                                </tr>
                                <tr style="border: hidden;">
                                    <th><b>Product Image:</b></th>
                                    <td><input type="file" name="productimage"></td>
                                </tr>
                                <tr style="border:hidden;">
                                    <th><b>Description:</b></th>
                                    <td><textarea name="description" cols="25" rows="3"></textarea></td>
                                </tr>
                                <tr style="border: hidden;">
                                    <th><b>Quantity:</b></th>
                                    <td><input type="number" name="productquantity"></td>
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
                                    <th><b>Product Category:</b></th>
                                    <td><select name="category" id="">
                                        <option value="select" selected disabled>select category</option>
                                        <option value="women kurta">Women kurta</option>
                                        <option value="women bottom wear">Women Bottom Wear</option>
                                        <option value="women party dress">Women Party Dress</option>
                                        <option value="women sports">Women Sports</option>
                                        <option value="women winter">Women winter wear</option>
                                        <option value="men topwear">Men Topwear</option>
                                        <option value="men bottomwear">men Bottomwear</option>
                                        <option value="men sports">Men sportswear</option>
                                        <option value="men winter">Men Winterwear</option>
                                        <option value="boys clothing">Boys Clothing</option>
                                        <option value="girls clothing">Girls Clothing</option>
                                        <option value="baby boy">Baby Boy</option>
                                        <option value="baby girl">Baby Girl</option>
                                    </select></td>
                                </tr>
                                <tr style="border: hidden;">
                                    <th><b>User Price:</b></th>
                                    <td><input type="float" name="uprice"></td> 
                                </tr>
                                <tr style="border: hidden;">
                                    <th><b>Wholesaler Price:</b></th>
                                    <td><input type="float" name="wprice"></td> 
                                </tr>
                                
                                <tr>
                                    <th></th>
                                    <!-- <td></td> -->
                                </tr>
                                <tr style="border: hidden;">
                                    <th></th>
                                    <td><input type="submit" name="addproduct" class="btn btn-success" value="AddProduct" style="font-size: 20px;margin-left: 60px;"></td>
                                </tr>
                            </table>
                        </form>
                    </div>
                    <div class="col-md-4"></div>
                </div>
            </div>
        </div>
    </body>
    </html>
""")

form=cgi.FieldStorage()
addproductt=form.getvalue("addproduct")
if addproductt != None:
    if len(form) != 0:
        productid = form.getvalue("productid")
        pproductname = form.getvalue("productname")
        pdescription = form.getvalue("description")
        pquantity = form.getvalue("productquantity")
        psize = form.getvalue("size")
        category = form.getvalue("category")
        uprice = form.getvalue("uprice")
        wprice = form.getvalue("wprice")
        productimagee = form['productimage']
        fn=os.path.basename(productimagee.filename)
        open("product/" + fn, "wb").write(productimagee.file.read())
        q="""insert into product(productid,productname,productimage,description,quantity,size,category,userprice,wholesalerprice) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(productid,pproductname,fn,pdescription,pquantity,psize,category,uprice,wprice)
        cur.execute(q)
        con.commit()
        print("""
                            <script>
                                alert("Product Added successfully!!");
                            </script>
                    """)



