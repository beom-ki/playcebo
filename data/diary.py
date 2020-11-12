#!python
# -*-coding:utf-8 -
print("content-type: text/html; charset=utf-8\r\n")

import sys, codecs, cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
Id = form["id"].value

DataRead = open('../database_'+Id , 'r', encoding="utf-8")
lines = DataRead.readlines() # database의 자료들을 list 형태로 저장
DateList = []
Today = []
Tomorrow = []
i = 0
if lines:
    while i < len(lines):
        if i % 3 == 0:
            DateList.append(lines[i])
        elif i % 3 == 1:
            Today.append(lines[i])
        else:
            Tomorrow.append(lines[i])
        i += 1
    TotalBody = ''
    for i in range(0,len(DateList)):
        TotalBody += '<h3>' +DateList[i]+ '</h3><ul><li>'+ Today[i]+ '</li><li>'+Tomorrow[i]+ '</li></ul>'
else:
    TotalBody = ''
print('''
    <!doctype html>
    <html lang="ko">
      <head>
          <meta charset="utf-8">
          <link rel="stylesheet" href="../diary.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src = "tablecolors.js"></script>
      </head>
      <body>
        <header>
          <input type="button" class="buttonindex" value="야간 모드" onclick="
            DayNightChanger(this);
          ">
          <input type = "button" class="buttonindex" value="맨 아래로 이동"id="top" onclick="location.href='#bottom'">
          <br>
        </header>
        <nav id="all">
            {TotalBody}
        </nav>
          <input type="button" value="맨 위로 이동"id="bottom" onclick="location.href='#top'">
          <a href = "../updateForDiary.py?id={Id}">오늘의 하루 추가하기</a>
      </body>
     </html>
'''.format(TotalBody = TotalBody, Id= Id))
