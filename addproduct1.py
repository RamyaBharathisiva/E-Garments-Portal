#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ride Seeker Details</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css">
    <style>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333;
}

form {
    margin-top: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
    color: #555;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="date"],
select,
textarea {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    margin-bottom: 10px;
}

select {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg fill="#555" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
    background-position: right 10px center;
    background-repeat: no-repeat;
    padding-right: 30px;
}

button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
}
.button-container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}


button:hover {
    background-color: #0056b3;
}

button:active {
    background-color: #004080;
}
</style>

</head>
<body>
    <div class="container">
        <h1>Ride Seeker Details</h1>
        <form enctype="multipart/form-data" method="POST">
            <!-- Personal Information -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" placeholder="Your name..." required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="Your email..." required>
            
            <label for="name">Password:</label>
            <input type="text" name="password" required>

            <label>Gender:</label>
            <input type="radio" value="male" name="gender">Male
            <input type="radio" value="female" name="gender">Female<br><br>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" placeholder="Your phone number..." required>

            <label for="">DOB</label>
            <input type="date" name=dob>

            <!-- Address Information -->
            <label for="">Address:</label>
            <textarea id="additional-info" name="address" placeholder="Address" rows="4"></textarea>

            <label for="">City:</label>
            <input type="text" id="" name="sity" placeholder="City" required>

            <label for="">State:</label>
            <input type="text" id="" name="state" placeholder="State" required>

            <!-- File Uploads -->
            <label for="photo">Photo:</label>
            <input type="file" name="photo"><br><br>

            <label for="id-proof">ID Proof:</label>
            <input type="file" name="idproof"><br><br>

            <!-- Form Actions -->
            <div class="button-container">
                <input type="submit" class="btn btn-primary" name="submit";>
                <input type="reset" class="btn btn-warning" name="reset">
            </div>
        </form>
    </div>
    </body>
</html>
""")



import cgi
import cgitb
import pymysql
import os

cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="garments")
cur=con.cursor()

form=cgi.FieldStorage()
psubmit=form.getvalue("submit")
if psubmit != None:
    if len(form) != 0:
        pname=form.getvalue("name")
        pemail=form.getvalue("email")
        ppassword=form.getvalue("password")
        pgender=form.getvalue("gender")
        pphone=form.getvalue("phone")
        pdob=form.getvalue("dob")
        paddress=form.getvalue("address")
        pcity=form.getvalue("city")
        pstate=form.getvalue("state")
        pphoto=form['photo']
        pidproof= form['idproof']

        if pphoto.filename:
            fn = os.path.basename(pphoto.filename)
            open("dbmedia/" + fn, "wb").write(pphoto.file.read())
            fn1 = os.path.basename(pidproof.filename)
            open("dbmedia/" + fn1, "wb").write(pidproof.file.read())
            sql = """insert into user(name,email,password,gender,phonenumber,dob,address,city,state,photo,id_proof) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (pname, pemail,ppassword, pgender, pphone, pdob, paddress, pcity, pstate, fn, fn1)
            cur.execute(sql)
            con.commit()
            print("""
                <script>
                    alert("register successfully");
                </script>  
            """)




            print("""
            <form action="" name="order" id="login">
                                  <div class="row">
                                    <div class="col-md-4">
                                        <img class="dress-card-img-top" src="%s" alt="img">
                                    </div>
                                    <div class="col-md-8" style="margin-top:10px;margin-left: 50px;">
                                        <h4 class="dress-card-title">%s</h4>
                                        <p class="dress-card-para" style="color: rgb(218, 27, 59);"><b>%s</b></p>
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
                                                <select name="quanity" id="" style="font-size: 20px;" onchange="myfun()" required>
                                                    <option value="select" selected disabled name="quantity">Quantity</option>
                                                    <option value="1">1</option>
                                                    <option value="2">2</option>
                                                    <option value="3">3</option>
                                                    <option value="4">4</option>
                                                </select>
                                            </div>
                                            
                                            <div class="form-group">
                                                <p class="dress-card-para"><b>Rs.%s</b></span></p>
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
                                                <input type="submit" class="btn" name="placeorder" value="Place Order" style="background-color:rgb(28, 108, 80);border: none;color:rgb(255, 253, 253);font-size: 20px;margin-top: 40px;border-radius: 2px;">
                                            </div>
                                        
                                    </div> 
                                   </div> 
                                </form>     
            
            
            
            
            
            
            
            
            """)