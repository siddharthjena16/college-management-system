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
print "<center><u><h1>Fees Database</h1></u></center>"
print "<br><br>"
print "<center><table cellpadding='10'>"
cursor = db.cursor()
sql="select * from dept"
cursor.execute(sql)
list2d = [list(i) for i in cursor.fetchall()]
print "<tr><td>Enter Student ID : </td><td><input type='text' name='StudId'></td></tr></table>"
print "<button type=submit formaction=fsid.py>SUBMIT</button></center>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
