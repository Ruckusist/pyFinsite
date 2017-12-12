#!/usr/bin/python3
import ccxt
import datetime

print("Content-type: text/html")
print("<html><head>")
print("<title>Kinetech Concepts</title>")
print("</head>")
print("<body bgcolor=#131116 text=red>")
print("<h1>Kinetech Concepts Financial Reports</h1>")
print("<br>")
print("Available Exchanges:")
print("<br>")
for i in ccxt.exchanges:
    print("/t| {} |".format(i))
    print("<br>")

print("</body></html>")
