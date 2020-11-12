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
        TotalBody += '<tr><td class="date">' +DateList[i]+ '</td><div class = "grid"><td class="range1">'+ RangeList[i]+ '</td><td><ul><li>'+FeelingList[i]+ '</li></ul></td></div></tr>'
else:
    TotalBody = ''

print('''
    <!doctype html>
    <html lang="ko">
      <head>
          <meta charset="utf-8">
          <title> 주식 </title>
          <link rel="stylesheet" href="tablestyle2.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src = "tablecolors.js"></script>
      </head>
      <body>
        <div class="bgimage"></div>
        <div class="content">
          <input type="button" value="야간 모드" onclick="
            DayNightChanger(this);
          ">
          <input type = "button" value="맨 아래로 이동"id="top" onclick="location.href='#bottom'">
          <br><br>
          <table>
            <thead>
              <tr>
                <th>날짜</th>
                <th>종목</th>
                <th>느낀 점, 결과</th>
              </tr>
            </thead>
            <tbody>
                {TotalBody}
            </tbody>
          </table>
        <input type="button" value="맨 위로 이동"id="bottom" onclick="location.href='#top'">
        <a href = "../updateForStock.py?id={Id}">오늘의 하루 추가하기</a>
      </body>
    </html>
'''.format(TotalBody = TotalBody, Id = Id))
