var Links = {
  setColor : function(color){
    var atags = document.querySelectorAll('a');
      atags.forEach(function(a){
        a.style.color=color;
      });
    var atags = document.querySelectorAll('a');
    var i=0;
    while(i < atags.length) {
      atags[i].style.color=color;
      i = i+1;
    }
    // $('a').css('color', color);
  }
};
var Body = {
  setColor : function(color){
    document.querySelector('body').style.color=color;
  },
  setBackgroundColor : function(color){
    document.querySelector('body').style.backgroundColor=color;
  }
};
var Background = {
  setImage : function(image) {
    document.body.style.backgroundImage=`url(${image})`;
    document.body.style.backgroundSize="100% 100%";
    document.body.style.backgroundRepeat="no-repeat";
  }
};

function DayNightChanger (self){
  if(self.value==='야간 모드'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    Links.setColor('white');
    Background.setImage('bgi5.jpg');
    self.value='주간 모드';
  }
  else{
    Body.setBackgroundColor('white');
    Body.setColor('black');
    Links.setColor('black');
    Background.setImage('bgi6.jpg');
    self.value='야간 모드';
  }
}

var now = new Date();
var hours = now.getHours();

function DayNightChangerAuto (){
  if(hours > 20 | hours < 7){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    Links.setColor('white');
    Background.setImage('bgi5.jpg');
    DayNight.value='주간 모드'
  }
  else{
    Body.setBackgroundColor('white');
    Body.setColor('black');
    Links.setColor('black');
    Background.setImage('bgi6.jpg');
    DayNight.value='야간 모드'
  }
}
