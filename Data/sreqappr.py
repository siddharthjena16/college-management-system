#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
print "Content-type: text/html"
form=cgi.FieldStorage()
StudId=form.getvalue('StudId')
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="select CourseId,Addr from studupreq where StudId='%s'"%(StudId)
cursor.execute(sql)
header = [i[0] for i in cursor.description]
list2d = [list(i) for i in cursor.fetchall()]
list2d.insert(0,header)
for row in list2d:
    pass
CourseId=unicode(row[0])
Addr=unicode(row[1])
cursor.close()
cursor = db.cursor()
sql="update stud set CourseId='%s',Addr='%s' where StudId='%s'"%(CourseId,Addr,StudId)
cursor.execute(sql)
db.commit()
cursor.close()
cursor = db.cursor()
sql="delete from studupreq where StudId='%s'"%(StudId)
cursor.execute(sql)
db.commit()
cursor.close()
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Students Database</h1></u></center>"
cursor = db.cursor()
sql="select StudId,CourseId,Addr from studupreq"
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
    if i!=0:
        newrow += u'<td align="center" style="padding:1px 4px"><input type=radio name="StudId" value="'+unicode(row[0])+'"'+u'</td>'
        newrow += u'<td align="center" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
    elif i==0:
        newrow += u'<td align="center" style="padding:1px 4px">'+u'</td>'
        newrow += u'<td align="center" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
    row.remove(row[0])
    newrow = newrow + ''.join([u'<td align="center" style="padding:1px 4px">' + unicode(x) + u'</td>' for x in row])  
    newrow += '</tr>' 
    htable+= newrow
htable += '</table>'
print htable
print "<br><br>"
print "<button type=submit formaction=sreqappr.py>Update</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=sreqreg.py>Reject</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<br><br>Updated"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
