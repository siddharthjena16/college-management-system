#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi, cgitb
form = cgi.FieldStorage()
Dept=form.getvalue('Dept')
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Courses Database</h1></u></center>"
sql="select CourseId,Cname,DName from courses c,dept d where c.deptid=d.deptid AND c.deptid='%s'" %(Dept)
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
cursor=db.cursor()
sql="select Dname from dept where DeptId='%s'"%(Dept) 
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
dname="lol";
for row in list2d:
    dname=unicode(row[0])
print "<tr><td>DName : </td><td>"+dname+"<input type=text name='Dept' value='%s' style='Display:none'>"%(Dept)+"</td></tr></table>"
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
