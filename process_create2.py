#!python
# -*-coding:utf-8 -
# print("content-type: text/html; charset=utf-8\r\n")

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


import cgi
form = cgi.FieldStorage()
newGoal = form["newGoal"].value

newGoalFile = open('iwilldo/'+newGoal+'.py', 'w')
newGoalFile.close()
newDatabase = open('database_'+newGoal, 'w')
newDatabase.close()


print("Location: index.py\n")
