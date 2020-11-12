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
RangeList = []
FeelingList = []
i = 0
if lines:
    while i < len(lines):
        if i % 3 == 0:
            DateList.append(lines[i])
        elif i % 3 == 1:
            RangeList.append(lines[i])
        else:
            FeelingList.append(lines[i])
        i += 1
    TotalBody = ''
    for i in range(0,len(DateList)):
        TotalBody += '<tr><td class="date">' +DateList[i]+ '</td><div class = "grid"><td class="range">'+ RangeList[i]+ '</td><td>'+FeelingList[i]+ '</td></div></tr>'
else:
    TotalBody = ''

print('''
  <!doctype html>
  <html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>선형대수학</title>
        <link rel="stylesheet" href="tablestyle.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src = "tablecolors.js"></script>
    </head>
    <body>
      <input type="button" value="야간 모드" onclick="
        DayNightChanger(this);
      ">
      <br> <br>
      <p class="monthindex"><a href="#8월">8월의 나</a></p>
      <p class="monthindex"><a href="#9월">9월의 나</a></p>
      <table>
        <thead>
          <tr>
            <th>날짜</th>
            <th>공부한 범위</th>
            <th>느낀 점, 다음 공부 계획</th>
          </tr>
        <tbody>
          {TotalBody}
        </tbody>
      </table>
      <a href = "../update.py?id={Id}">오늘의 하루 추가하기</a>
    </body>
  </html>
  '''.format(TotalBody = TotalBody, Id = Id))
