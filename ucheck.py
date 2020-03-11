#!/python27/python
import MySQLdb
import cgi, cgitb
form = cgi.FieldStorage()
uname=form.getvalue('uname')
passw=form.getvalue('pass')
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor1=db.cursor(MySQLdb.cursors.SSCursor)
sql= "select uname from user where uname='%s'" %uname
cursor1.execute(sql)
resultu=cursor1.fetchone()
cursor1.close()
cursor = db.cursor(MySQLdb.cursors.SSCursor)
sql= "select pass from user where uname='%s'" %uname
cursor.execute(sql)
resultp=cursor.fetchone()
cursor.close()
admin=1
data=2
stud=3
appr='y'
if resultu==None:
    print "Location: indexfail.html"
    print "Content-type:text/html\r\n\r\n"
elif uname in resultu :
    if (passw in resultp):
        cursor=db.cursor(MySQLdb.cursors.SSCursor)
        sql="select approved from user where uname='%s'"%(uname)
        cursor.execute(sql)
        approved=cursor.fetchone()
        cursor.close()
        if (appr in approved):
            cursor=db.cursor(MySQLdb.cursors.SSCursor)
            sql="select utid from user where uname='%s'"%(uname)
            cursor.execute(sql)
            resultut=cursor.fetchone()
            cursor.close()
            if(admin in resultut):
                print "Location: Admin/homeadmin.html"
                print "Content-type:text/html\r\n\r\n"
            if(data in resultut):
                print "Location: Data/homedata.html"
                print "Content-type:text/html\r\n\r\n"
            if(stud in resultut):
                print "Content-type:text/html\r\n\r\n"
                print """<html><body onLoad="sub.dispatchEvent(new MouseEvent('click'))">"""
                print "<form type=get action='Stud/homestud.py'><input type=text name='StudId' style='display:none' value='"+uname+"'><button type=submit id='sub'></button></form>"
                print "</body></html>"
        else:
            print "Location: indexfail.html"
            print "Content-type:text/html\r\n\r\n"
    else:
        print "Location: indexfail.html"
        print "Content-type:text/html\r\n\r\n"
else:
        print "Location: indexfail.html"
        print "Content-type:text/html\r\n\r\n"
