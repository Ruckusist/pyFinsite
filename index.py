#!/usr/bin/python3
import ccxt

print("Content-type: text/html")
print("<html><head/>")
print("<body>")
print("Kinetech Concepts Financial Reports")
print("<br>")
print("Available Exchanges:")
print("<br>")
for i in ccxt.exchanges:
    print("/t| {} |".format(i))
    print("<br>")

print("</body></html>")
