#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="automatedgarments")
cur = con.cursor()
q = """select * from wholesaler"""
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    print("""
       <form>
            <input type="hidden" value="%s" name="uname">
            <input type="hidden" value="%s" name="password">
        </form> 
       """ % (i[1], i[19]))

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
    <style>
        #logo {
  height: 350px;
  width: 350px;
  margin-top: -49%;
}
body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        margin-left: 25%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 600px;
                        width: 50%;
                        background-color:bisque;
                    }

                    h2 {
                        color: #ccc;
                    }

                    .login-container {
                        background-color: white;
                        padding: 80px;
                        border-radius: 8px;
                        box-shadow: 5px 7px 6px rgba(19, 8, 8, 1);
                    }

                    .form-group {
                        margin-bottom: 15px;
                    }

                    .form-group label {
                        display: block;
                        font-weight: bold;
                    }

                    .form-group input {
                        width: 100%;
                        padding: 8px;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                    }

                    .form-group button {
                        width: 100%;
                        padding: 8px;
                        background-color: #38d63e;
                        color: white;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }

                    .form-group a {
                        display: block;
                        text-align: center;
                        text-decoration: none;
                        color: #333;
                        margin-top: 10px;
                    }



    </style>

</head>
<body>
    <div class="container">
        <nav class="navbar navbar" style="font-size: 10px;box-shadow: 0px 5px 20px -10px rgb(0, 0, 0);">
            <div class="container-fluid">

                <a href="home.py" class="navbar-brand mx-auto">
                    <img src="assets/Logo2.png" id="logo" alt="logo" class="navbar-brand" height=-"200px">
                </a>
                <div class="navbar-right">

                </div>

            </div>

        </nav>
                    <h2></h2>
                    <div class="login-container">
                        <h3>Forget Password </h3><br><br>
                        <form action="" method="post" enctype="multipart/form-data">
                            <div class="form-group">

                                <label for="username">User Mailid:</label>
                                <input type="text" name="userid" placeholder="Enter your mailid" id="hover1"
                                    class="form-control"><br><br>

                                <input type="submit" id="example" name="submit" value="Submit" class="btn btn-primary"> 

                            </div>
                        </form>



                    </div>
                </div>
        </div>
        </body>
        </html>
                """)

form = cgi.FieldStorage()
username = form.getvalue("userid")
submit = form.getvalue("submit")
if submit != None:
    x = """Select password from wholesaler where email="%s" """ % (username)
    cur.execute(x)
    passw = cur.fetchone()
    formadd = "ramyabharathi.242002@gmail.com"
    password = "oshiotvoqktvvjpa"
    toadd = username
    subject = "StyleSphere"
    body = "welcome!!!\n This is your Password:{}".format(passw)
    mes = "subject:{}\n\n{}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(formadd, password)
    server.sendmail(formadd, toadd, mes)
    server.quit()
    print("""
        <script>
            alert("Email Sent successfully");
        </script>""")




