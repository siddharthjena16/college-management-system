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
print "<center><u><h1>Courses Database</h1></u></center>"
print "<br><br>"
print "<center><table cellpadding='10'>"
cursor = db.cursor()
sql="select * from dept"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>Select Department : </td><td><select name='Dept'>"
for row in list2d:
    print "<option value="+unicode(row[0])+">"+unicode(row[1])+"</option>"    
print "</select></td></tr></table>"
print "<button type=submit formaction=cdept.py>SUBMIT</button></center>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
