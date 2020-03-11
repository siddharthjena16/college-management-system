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
print "<center><u><h1>Users Database</h1></u></center>"
sql="select UserId,Uname,Pass,utname AS 'User Type',Approved from user,utype where user.utid=utype.utid"
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
        newrow += u'<td align="center" style="padding:1px 4px"><input type=radio name="UserId" value="'+unicode(row[0])+'"'+u'</td>'
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
print "<tr><td>User Name : </td><td><input type=text name='UName'></td></tr>"
print "<tr><td>Password : </td><td><input type=password name='Pass'></td></tr>"
cursor = db.cursor()
sql="select utid,utname from utype"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>User Type : </td><td><select name='utid'>"
for row in list2d:
    print "<option value="+unicode(row[0])+">"+unicode(row[1])+"</option>"    
print "</select></td></tr>"
print "<tr><td>Approved : </td><td><select name='appr'><option value='y'>YES</option><option value='n'>NO</option></select></td></tr></table>"
print "<button type=submit formaction=usersins.py>INSERT</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=usersdel.py>DELETE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=usersup.py>UPDATE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
