#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable
import os
from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie


#question 4
#print("Content-Type: text/html")
#print()
#print(login_page())




#question 1
print(os.environ)
#question2
print(os.environ["HTTP_COOKIE"])

#question3 
print(os.environ["HTTP_USER_AGENT"])

#question4 
print(os.environ["QUERY_STRING"])
print("Content-Type: text/html")
print(login_page())
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

#question5 
form_ok = username == secret.username and password == secret.password
c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value
cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password
if form_ok:
    print("Set-Cookie: username= ", username)
    print("Set-Cookie: password= ", password)
#print()


#q6

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username,password))
else:
    print(after_login_incorrect())
print()
