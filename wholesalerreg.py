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
    
</head>
<body>
    <form id="login" onsubmit="wholesaler()" method="post" enctype="multipart/form-data">
        <div class="form-group" style="margin-left: 77px;">
            <input type="text" name="ownername" placeholder="Owner Name" style="height: 40px;width:400px">
    
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Gender<input type="radio" id="wgender" name="wgender" style="margin-left: 20px;" value="Male">
            Male<input type="radio" id="ugender" name="wgender" style="margin-left: 20px;" value="Female">
            Female
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="email" id="wemail" name="wemail" placeholder="Emailid" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="date" id="wdob" name="wdob" placeholder="DOB" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="number" id="wphno" name="wphno" placeholder="phone number" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Upload Your Photo<input type="file" name="wphoto" id="wphoto" style="margin-top: 10px;">    
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" id="shopname" name="shopname" placeholder="Shopname" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Shop licence<input type="file" name="licence" id="licence" style="margin-top: 10px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Shop Image<input type="file" name="shopimage" id="shopimage" style="margin-top: 10px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            Aadhaar card<input type="file" name="aadhaar" id="aadhaar" style="margin-top: 10px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" name="wdoor" id="wdoor" placeholder="Door Number" style="height: 40px;width: 400px;">  
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" name="wstreet" id="wstreet" placeholder="street" style="height: 40px;width: 400px;">  
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" name="wcity" id="wcity" placeholder="City" style="height: 40px;width: 400px;">  
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" name="wdistrict" id="wdistrict" placeholder="District" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="text" name="wstate" id="wstate" placeholder="State" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="number" name="wpincode" id="wpincode" placeholder="Pincode" style="height: 40px;width: 400px;">
        </div>
        <div class="form-group" style="margin-left: 80px;">
            <input type="submit" class="btn btn-success" name="wsubmit" value="Register" style="width:30%;width: 400px;">
        </div>
    </form>
</body>
</html>





""")
form = cgi.FieldStorage()
wsubmit=form.getvalue("wsubmit")
if wsubmit != None:
    if len(form) != 0:
            ownername=form.getvalue("ownername")
            wgender=form.getvalue("wgender")
            wemail=form.getvalue("wemail")
            wdob=form.getvalue("wdob")
            wphno=form.getvalue("wphno")
            wphoto=form["wphoto"]
            shopname=form.getvalue("shopname")
            licence=form["licence"]
            shopimage=form["shopimage"]
            aadhaarcard=form["aadhaar"]
            udoor = form.getvalue('wdoor')
            ustreet = form.getvalue('wstreet')
            ucity = form.getvalue('wcity')
            udistrict = form.getvalue('wdistrict')
            ustate = form.getvalue('wstate')
            upincode = form.getvalue('wpincode')

            if wphoto.filename and licence.filename and shopimage.filename and aadhaarcard.filename:
                    fn1 = os.path.basename(wphoto.filename)
                    open("dbmedia/" + fn1, "wb").write(wphoto.file.read())
                    fn2 = os.path.basename(licence.filename)
                    open("dbmedia/" + fn2, "wb").write(licence.file.read())
                    fn3 = os.path.basename(shopimage.filename)
                    open("dbmedia/" + fn3, "wb").write(shopimage.file.read())
                    fn4 = os.path.basename(aadhaarcard.filename)
                    open("dbmedia/" + fn4, "wb").write(aadhaarcard.file.read())
                    q="""insert into wholesaler(ownername,gender,email,dob,phno,photo,shopname,shoplicence,shopimage,aadhaarcard,door,street,city,district,state,pincode)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(ownername,wgender,wemail,wdob,wphno,fn1,shopname,fn2,fn3,fn4,udoor,ustreet,ucity,udistrict,ustate,upincode)
                    cur.execute(q)
                    con.commit()
                    print("""
                                        <script>
                                            alert("Registered successfully!!")
                                        </script>
                                """)