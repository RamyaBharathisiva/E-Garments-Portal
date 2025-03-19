#!C:/Users/ramya/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os
import smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="testcase")
cur = con.cursor()
print("""
<form method="post" enctype="multipart/form-data">
<input type="text" name="name">
<input type="file" name="images">
<input type="submit" name="submit">
</form>""")
form=cgi.FieldStorage()
sub=form.getvalue("submit")
if sub != None:
    if len(form) != 0:
        name=form.getvalue("name")
        pimage=form['images']
  
        if pimage.filename:
            fn=os.path.basename(pimage.filename)
            open("sample/"+fn,"wb").write(pimage.file.read())
            q="""insert into sample(name,profile)values('%s','%s')""" %(name,fn)
            cur.execute(q)
            con.commit()
            print("""
    
    <script>
    alert("success");
    </script>
    """)