#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Students Database</h1></u></center>"
sql="select StudId,Sname,Addr,DOB,DOJ,CName,FatherName,MotherName,Remarks from stud s,courses c where s.CourseId=c.CourseId"
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
print "<table cellpadding='10'>"
print "<tr><td>SName : </td><td><input type=text name='SName'></td></tr>"
print "<tr><td>Addr : </td><td><textarea name='Addr' placeholder='Address'></textarea></td></tr>"
print "<tr><td>DOB (YYYY-MM-DD): </td><td><input type=date name='DOB'></td></tr>"
print "<tr><td>DOJ (YYYY-MM-DD): </td><td><input type=date name='DOJ'></td></tr>"
cursor = db.cursor()
sql="select CourseId,Cname from courses"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>CName : </td><td><select name='CourseId'>"
for row in list2d:
    print "<option value="+unicode(row[0])+">"+unicode(row[1])+"</option>"    
print "</select></td></tr>"
print "<tr><td>FatherName : </td><td><input type=text name='FatherName'></td></tr>"
print "<tr><td>MotherName : </td><td><input type=text name='MotherName'></td></tr>"
print "<tr><td>Remarks : </td><td><input type=text name='Remarks'></td></tr></table>"
print "<button type=submit formaction=studins.py>INSERT</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=studdel.py>DELETE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=studup.py>UPDATE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
