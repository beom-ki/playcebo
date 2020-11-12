#!python
# -*-coding:utf-8 -
print("content-type: text/html; charset=utf-8\r\n")

import sys, codecs, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
Id = form["id"].value

print('''
<!doctype html>
<html lang="ko">
  <head>
      <meta charset="utf-8">
      <title>{Id}</title>
      <link rel="stylesheet" href="tablestyle.css">
  </head>
  <body>
    <form action="process_updateForDiary.py?id={Id}" method="post">
      <table>
        <thead>
          <tr>
            <th>날짜</th>
            <th>오늘 하루</th>
            <th>내일의 목표</th>
          </tr>
        <tbody>
          <tr>
            <td class="date"> <input type="text" name="date">
            </td>
            <div class="grid">
              <td class="range"> <textarea rows="1" name="range"></textarea>
              </td>
              <td class="range"> <textarea rows="1" placeholder="Enter 사용하지 마세요" name="feeling"></textarea>
              </td>
            </div>
          </tr>
        </tbody>
      </table>
      <input type="submit" value="추가하기">
     </form>
</body>
</html>
'''.format(Id = Id))
