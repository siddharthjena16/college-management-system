#!/python27/python
import MySQLdb
import cgi, cgitb
from head import *
from side import *
from foot import *
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
form = cgi.FieldStorage()
FeesId=form.getvalue('FeesId')
sql="delete from fees where FeesId='%s'" %(FeesId)
cursor.execute(sql)
db.commit()             
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Fees Database</h1></u></center>"
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="select * from fees"
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
        newrow += u'<td align="center" style="padding:1px 4px"><input type=radio name="FeesId" value="'+unicode(row[0])+'"'+u'</td>'
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
print "<tr><td>StudID : </td><td><input type=text name='StudId'></td></tr>"
print "<tr><td>DOP (YYYY-MM-DD): </td><td><input type=date name='DOP'></td></tr>"
print "<tr><td>Amount : </td><td><input type=text name='Amount'></td></tr>"
print "<tr><td>Remarks : </td><td><input type=text name='Remarks'></td></tr></table>"
print "<button type=submit formaction=feesins.py>INSERT</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=feesdel.py>DELETE</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "<button type=submit formaction=feesup.py>UPDATE</button>"
print "<br><br>"
print "<button type=submit formaction=fprint.py style='padding-right:20px;padding-left:20px'>PRINT</button>"
print "</center></form>"
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
