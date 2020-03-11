#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
form=cgi.FieldStorage()
StudId=form.getvalue('StudId')
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Fees Database</h1></u></center>"
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="select * from fees where studid='%s'"%(StudId)
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
print "<input type=text style='display:none' name='Remarks' value='None'>"
print "<table cellpadding='10'>"
print "<tr><td>Fees Id(Receipt No.) : </td><td><input type=text name='FeesId'></td></tr>"
print "<tr><td>DOP (YYYY-MM-DD): </td><td><input type=date name='DOP'></td></tr>"
print "<tr><td>Amount : </td><td><input type=text name='Amount'></td></tr></table>"
print "<input type=text name='StudId' style='display:none' value='"+StudId+"'><button style='display:none' type=submit id='subh' formaction='homestud.py'><button style='display:none' type=submit id='subs' formaction='s1.py'></button><button style='display:none' type=submit id='subf' formaction='f1.py'></button>"
print "<button type=submit formaction=feesub.py>Submit Fees</button>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
