#!/usr/bin/python3

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import cgi
import requests
import re

import mysql.connector

print("Content-Type: text/html")   
print("")                          

form = cgi.FieldStorage()
text = form.getvalue('text','')

#if (text==""):
print("<form action=\"mysqlsample.py\">")
print("<input type=text name=\"text\">")
print("<input type=submit>")
print("</form>")

mydb = mysql.connector.connect(
  host="localhost",
  database="gk9999",
  user="gk9999",
  password="gk9999"
)

mycursor = mydb.cursor()
sql="select * from country where cname LIKE '%" + text + "%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  print("<br>\n")

#for row in myresult:
#    print(row['cname'])
#    print(row['capital'])
