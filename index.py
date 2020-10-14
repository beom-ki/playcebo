#!python
# -*-coding:utf-8 -*
print("content-type: text/html; charset=utf-8\r\n")
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# 구글링을 통해 위 방법으로 해결하면 된다는 것을 알게 되었다!
import cgi, os

iamdoingList = []
# myorder = [2, 1, 6, 5, 4, 3, 7, 0]
for file in os.listdir('iamdoing'):
    if file.endswith(".py"):
        iamdoingList.append(file)
# iamdoingList = [iamdoingList[i] for i in myorder]

iamdoingLink = ''
for task in iamdoingList:
    if task.endswith(".py"):
        name = task.rstrip('.py')
    iamdoingLink = iamdoingLink + '<li><a href="iamdoing/{link}?id={name}">{name}</a></li>'.format(link= task, name=name)

iwilldoList = []
for file in os.listdir('iwilldo'):
    if file.endswith(".html") or file.endswith(".py"):
        iwilldoList.append(file)

iwilldoLink = ''
for task in iwilldoList:
    if task.endswith(".html"):
        name = task.rstrip('.html')
        iwilldoLink = iwilldoLink + '<li><a href="iwilldo/{name}.html">{name}</a></li>'.format(name = name)
    else:
        name = task.rstrip('.py')
        iwilldoLink = iwilldoLink + '<li>{name}</li>'.format(name = name)
# form = cgi.FieldStorage()
# if 'id' in form:
#     pageId = form["id"].value
#     open("data/"+pageId+".html", 'r').read()
# else:
#     pageId = "index"
#     open("data/index.html", 'r').read()
print('''<!doctype html>
<html lang="ko">
  <head>
      <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
      <title>playcebo</title>
      <link rel="stylesheet" href="style.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src = "colors.js"></script>
  </head>
  <body id="body">
    <header>
      <nav>
        <h1><a href="data/def.html" class="noline"> Playcebo </a></h1>
      </nav>
      <input type="button" id="DayNight" value="야간 모드" onclick="
        DayNightChanger(this);
      ">
      <h3 class="intro"> ★자기계발을 놀면서 하자★ </h3>
      <p class="intro">　앞으로 제 하루의 일기와 자기계발 일지를 작성해나갈 예정입니다. <br>
        같이 참여하면서 서로 동기부여해봐요! </p>
      <br>
    </header>
    <article>
    <p class="diary"><a href="data/diary.py?id=diary"> 오늘의 일기, 내일의 목표 </a></p>
      <div id="total"> <!-- article은 본문 내용 위치하는 곳에 표시 -->
        <section id="imdoing">
          <h3 class="indent"><mark> ★자기계발 목록★ </mark></h3>
          <nav>
            <ol>
              {iamdoingLink}
              <form action="process_create.py" method="post">
                  <li> <input type= "text" name= "newTask" placeholder= "더 추가하기"> <input type="submit" value="확정"> <!-- name값으로 데이터 전송 -->
                  </li>
              </form>
            </ol>
          </nav>
        </section>
        <section id="illdo">
          <h3 class="indent"><mark>★앞으로 하고 싶은 것들★</mark></h3>
          <nav>
            <ol>
              {iwilldoLink}
              <form action="process_create2.py" method="post">
                  <li> <input type= "text" name= "newGoal" placeholder= "더 추가하기"> <input type="submit" value="확정">
                  </li>
              </form>
           </ol>
         </nav>
        </section>
      <div>
    </article>
    <footer>
      <input type="button" id="login" value="나도 참여하기" onclick="location.href='data/own.html'">
    </footer>
    <script>
      DayNightChangerAuto();
    </script>
  </body>
</html>
'''.format(iamdoingLink = iamdoingLink, iwilldoLink = iwilldoLink))
