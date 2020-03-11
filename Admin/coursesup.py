#!/python27/python
import MySQLdb
import cgi, cgitb
from head import *
from side import *
from foot import *
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
form = cgi.FieldStorage()
CourseId=form.getvalue('CourseId')
Cname=form.getvalue('CName')
DeptId=form.getvalue('Dept')
sql="update courses set CName='%s',DeptId='%s' where CourseId='%s'" %(Cname,DeptId,CourseId)
cursor.execute(sql)
db.commit()
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Courses Database</h1></u></center>"
sql="select CourseId,Cname,DName from courses c,dept d where c.deptid=d.deptid"
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
        newrow += u'<td align="center" style="padding:1px 4px"><input type=radio name="CourseId" value="'+unicode(row[0])+'"'+u'</td>'
    elif i==0:
        newrow += u'<td align="center" style="padding:1px 4px">'+u'</td>'
    else:
        newrow += u'<td align="center" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
    row.remove(row[0])
    newrow = newrow + ''.join([u'<td align="center" style="padding:1px 4px">' + unicode(x) + u'</td>' for x in row])  
    newrow += '</tr>' 
    htable+= newrow
htable += '</table>'
print htable
cursor.close()
print "<br><br>"
print "<table cellpadding='10'>"
print "<tr><td>CName : </td><td><input type=text name='CName'></td></tr>"
cursor = db.cursor()
sql="select * from dept"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>DName : </td><td><select name='Dept'>"
for row in list2d:
    print "<option value="+unicode(row[0])+">"+unicode(row[1])+"</option>"    
print "</select></td></tr></table>"
print "<button type=submit formaction=coursesins.py>INSERT</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=coursesdel.py>DELETE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=coursesup.py>UPDATE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"


