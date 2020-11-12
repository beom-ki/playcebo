#!python
# -*-coding:utf-8 -
# print("content-type: text/html; charset=utf-8\r\n")

import sys, codecs, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
Id = form["id"].value
Date = form["date"].value
Range = form["range"].value
Feeling = form["feeling"].value

DatabaseFile = open('database_'+Id,'a',encoding="utf-8")
DatabaseFile.write(Date+'\n')
DatabaseFile.write(Range+'\n')
DatabaseFile.write(Feeling+'\n')
DatabaseFile.close()

print("Location: iamdoing/{Id}.py?id={Id}\n".format(Id=Id))
