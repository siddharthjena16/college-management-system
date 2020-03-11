#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
form=cgi.FieldStorage()
FeesId=form.getvalue('FeesId')
print "Content-type: text/html"
Heading()
print "<body>"
print "<div class='container'>"
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="select FeesId,SName,DOP,Amount,Remark from fees,stud where FeesId='%s' and stud.StudId=fees.StudId"%(FeesId)
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
for row in list2d:
    pass
print "<center>"
htable=u'<table border="0" bordercolor=000000 cellspacing="0" bgcolor="#FFA500" cellpadding="15" style="table-layout:fixed;vertical-align:bottom;font-size:20px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130);width:100%" >'
htable+='<tr><td colspan=2><center><u><b>LIIT</b></u><br>Mattancherry</center></td></tr>'
htable+='<tr><td align="left">Receipt No. '+unicode(row[0])+'</td><td align="right">Date '+unicode(row[2])+'</td></tr>'
htable+='<tr><td colspan=2><center><b><u>Receipt</u></b></center></td></tr>'
htable+='<tr><td colspan=2>Received Rs. <b>'+unicode(row[3])+'</b> from <b>'+unicode(row[1])+'</b> with thanks.</td></tr>'
htable+='<tr><td colspan=2 align="right"><br>Authority Signature</td></tr>'
htable+='</table>'
print htable
print "<br><br><button onclick='window.print()'>Print</button>"
print "<br><br><a href='home.html' style='float:right'>Go back to Home</a>"
print "</center>"
print "<!-- end .content --></div></div>"

print "</body>"
print "</html>"
