var Links = {
  setColor : function(color){
    var atags = document.querySelectorAll('a');
      atags.forEach(function(a){
        a.style.color=color;
      });
    <!--
    var atags = document.querySelectorAll('a');
    var i=0;
    while(i < atags.length) {
      atags[i].style.color=color;
      i = i+1;
    }
    -->
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
var Border = {
  setColor : function(width_color){
    // var ths = document.querySelectorAll('th');
    // var i = 0 ;
    // while(i < ths.length) {
    //   ths[i].style.border=width_color;
    //   i = i+1;
    // }
    // var tds = document.querySelectorAll('td');
    // var i = 0 ;
    // while(i < tds.length) {
    //   tds[i].style.border=width_color;
    //   i = i+1;
    // }
    $('th').css('border', width_color);
    $('td').css('border', width_color);
  }
};
var Background = {
  setImage : function(image) {
    document.body.style.backgroundImage=`url(${image})`;
    document.body.style.backgroundSize="100% 100%";
  }
};

function DayNightChanger (self){
  if(self.value==='야간 모드'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    Links.setColor('white');
    Border.setColor('0.5px solid white');
    Background.setImage('bgi5.jpg');
    self.value='주간 모드';
  }
  else{
    Body.setBackgroundColor('white');
    Body.setColor('black');
    Links.setColor('black');
    Border.setColor('1.5px solid black');
    Background.setImage('bgi9.jpg');
    self.value='야간 모드';
  }
}
