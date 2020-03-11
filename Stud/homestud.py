#!/python27/python
import MySQLdb
from head import *
from side import *
from foot import *
import cgi,cgitb
print "Content-type: text/html"
Heading()
print "<body>"
form=cgi.FieldStorage()
StudId=form.getvalue('StudId')
print "<form type=get><input type=text name='StudId' style='display:none' value='"+StudId+"'><button style='display:none' type=submit id='subh' formaction='homestud.py'><button style='display:none' type=submit id='subs' formaction='s1.py'></button><button style='display:none' type=submit id='subf' formaction='f1.py'></button>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
