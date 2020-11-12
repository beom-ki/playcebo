#!python
# -*-coding:utf-8 -
# print("content-type: text/html; charset=utf-8\r\n")

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


import cgi
form = cgi.FieldStorage()
newTask = form["newTask"].value

newTaskFile = open('iamdoing/'+newTask+'.py', 'w')
newTaskFile.close()
newDatabase = open('database_'+newTask, 'w')
newDatabase.close()

print("Location: index.py\n")
