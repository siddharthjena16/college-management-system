#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
form=cgi.FieldStorage()
StudId=form.getvalue('StudId')
CourseId=form.getvalue('CourseId')
Addr=form.getvalue('Addr')
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="insert into studupreq values('%s','%s','%s')"%(StudId,CourseId,Addr)
cursor.execute(sql)
db.commit()
cursor.close()
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Students Database</h1></u></center>"
cursor = db.cursor()
sql="select StudId,Sname,Addr,DOB,DOJ,CName,FatherName,MotherName,Remarks from stud s,courses c where s.CourseId=c.CourseId AND StudId='%s'"%(StudId)
cursor.execute(sql)
header = [i[0] for i in cursor.description]
list2d = [list(i) for i in cursor.fetchall()]
list2d.insert(0,header)
print "<center>"
htable=u'<table border="1" bordercolor=000000 cellspacing="0" bgcolor="#FFA500" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:20px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]] 
i=-1
for row in list2d:
    i+=1;
    newrow = u'<tr>'
    newrow += u'<td align="center" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
    row.remove(row[0])
    newrow = newrow + ''.join([u'<td align="center" style="padding:1px 4px">' + unicode(x) + u'</td>' for x in row])  
    newrow += '</tr>' 
    htable+= newrow
htable += '</table>'
print htable
print "<br><br>"
print "<table cellpadding='10'>"
print "<tr><td>Addr : </td><td><textarea name='Addr' placeholder='Address'></textarea></td></tr>"
cursor.close()
cursor = db.cursor()
sql="select CourseId,Cname from courses"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>CName : </td><td><select name='CourseId'>"
for row in list2d:
    print "<option value="+unicode(row[0])+">"+unicode(row[1])+"</option>"    
print "</select></td></tr>"
print "</table>"
print "Request submitted. Check after 2-3 days. If request not approved, approach office"
print "<br><button type=submit formaction=studupreq.py>Request Update</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<input type=text name='StudId' style='display:none' value='"+StudId+"'><button style='display:none' type=submit id='subh' formaction='homestud.py'><button style='display:none' type=submit id='subs' formaction='s1.py'></button><button style='display:none' type=submit id='subf' formaction='f1.py'></button>"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
