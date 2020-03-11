#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
form=cgi.FieldStorage()
From=form.getvalue('From')
To=form.getvalue('To')
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Fees Report</h1></u></center>"
db = MySQLdb.connect("localhost","root","liitliit","school" )
cursor = db.cursor()
sql="select DOP AS Date,FeesId,concat('Paid by ',SName) AS Particulars, Amount from fees,stud where DOP BETWEEN '%s' AND '%s' AND fees.studid=stud.studid ORDER BY FeesId ASC"%(From,To)
cursor.execute(sql)
header = [i[0] for i in cursor.description]
list2d = [list(i) for i in cursor.fetchall()]
list2d.insert(0,header)
print "<center>"
htable=u'<table border="1" bordercolor=000000 cellspacing="0" bgcolor="#FFA500" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:20px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
htable+='<tr><td colspan=4><center><b><u>LIIT</b></u><br>Mattancherry<br><u>Fees Register</u></center></td>'
list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]] 
i=-1
for row in list2d:
    newrow = u'<tr>'
    newrow += u'<td align="center" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
    row.remove(row[0])
    newrow = newrow + ''.join([u'<td align="center" style="padding:1px 4px">' + unicode(x) + u'</td>' for x in row])  
    newrow += '</tr>' 
    htable+= newrow
cursor.close()
cursor=db.cursor()
sql="select SUM(Amount) from fees where DOP BETWEEN '%s' AND '%s'"%(From,To)
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
for row in list2d:
        pass
htable+='<tr><td></td><td></td><td><center>Total : </td><td><center>'+unicode(row[0])+'</td></tr>'
htable += '</table>'
print htable
print "<br><br>"
print "</center></form>"
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
