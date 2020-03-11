#!/python27/python
import MySQLdb
import cgi, cgitb
from head import *
from side import *
from foot import *
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
form = cgi.FieldStorage()
DeptId=int(form.getvalue('DeptId'))
DName=form.getvalue('DName')
sql="update dept set Dname='%s' where DeptId=%d" %(DName,DeptId)
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
print "<center><u><h1>Departments Database</h1></u></center>"
sql="select * from dept"
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
        newrow += u'<td align="center" style="padding:1px 4px"><input type=radio name="DeptId" value="'+unicode(row[0])+'"'+u'</td>'
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
print "<br><br>"
print "DName : <input type='text' name='DName'><br><br>"
print "<button type=submit formaction=deptins.py>INSERT</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=deptdel.py>DELETE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=deptup.py>UPDATE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"

