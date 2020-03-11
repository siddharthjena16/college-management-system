#!/python27/python
from head import *
from side import *
from foot import *
print "Content-type: text/html"
Heading()
print "<body>"
side()
print "<div class='content'><!-- TemplateBeginEditable name='EditRegionContent' --><!-- TemplateEndEditable -->"
print "<form type=get>"
print "<center><u><h1>Fees Database</h1></u></center>"
print "<br><br>"
print "<center><table cellpadding='10'>"
print "<tr><td colspan=2><center><b>Enter date range</b></center></td></tr>"
print "<tr><td>From : <input type='date' name='From'></td><td>To : <input type='date' name='To'></td></tr>"   
print "</table>"
print "<br><button type=submit formaction=frep.py>SUBMIT</button></center>"
print "&nbsp;&nbsp;&nbsp;&nbsp;"
print "</center></form>"    
print "<!-- end .content --></div>"
foot()
print "</body>"
print "</html>"
