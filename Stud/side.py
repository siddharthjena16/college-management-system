#!/python27/python
import cgi,cgitb
def side():
	print "<script>"
	print "function studin(){"
	print "document.getElementById('studsub').style.display='block';"
	print "}"
	print "function studout(){"
	print "document.getElementById('studsub').style.display='none';"
	print "}"
	print "function cin(){"
	print "document.getElementById('csub').style.display='block';"
	print "}"
	print "function cout(){"
	print "document.getElementById('csub').style.display='none';"
	print "}"
	print "function fin(){"
	print "document.getElementById('fsub').style.display='block';"
	print "}"
	print "function fout(){"
	print "document.getElementById('fsub').style.display='none';"
	print "}"
	print "</script>"
	print "<div class='container'>"
	print "<div class='header'>"
	print "<div class='lhead'>"
	print "<a href='#'><img src='../img_avatar2.png' alt='Insert Logo Here' name='Insert_logo' width='180' height='90' id='Insert_logo' style='background: #C6D580; display:block;' /></a>"
	print "</div>"
	print "<div class='rhead'>"
	print "<h1>College Management Systsem</h1>"
	print "</div>"
	print "<!-- end .header --></div>"
	print "<div class='sidebar1'>"
	print "<ul class='nav'>" 
	print """<li><a onclick="subh.dispatchEvent(new MouseEvent('click'))">Home</a></li>"""
	print """<li><a onclick="subs.dispatchEvent(new MouseEvent('click'))">Student Info</a></li>"""
	print """<li><a onclick="subf.dispatchEvent(new MouseEvent('click'))">Fees Paid</a></li>"""
	print "<li><a href='../index.html'>Logout</a></li>"
	print "</ul></form>"
	print "<div style='height: auto'>"
	print "<p> College Management System is web application for managing day to day activity of the College</p>"
	print "</div>"
	print "<!-- end .sidebar1 --></div>"