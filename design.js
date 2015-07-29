$(window).load(function () {
    $("#English").hover(function(){
      $('#English').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#English").mouseleave(function(){
      $('#English').stop().animate({ "margin-left": '56%' }, {queue: false});
    });
    $("#Math").hover(function(){
      $('#Math').stop().animate({ "margin-left": '66%' }, {queue: false});
    });
    $("#Math").mouseleave(function(){
      $('#Math').stop().animate({ "margin-left": '60%' }, {queue: false});
    });
    $("#Humanities").hover(function(){
      $('#Humanities').stop().animate({ "margin-left": '49%' }, {queue: false});
    });
    $("#Humanities").mouseleave(function(){
      $('#Humanities').stop().animate({ "margin-left": '55%' }, {queue: false});
    });
    $("#Science").hover(function(){
      $('#Science').stop().animate({ "margin-left": '46%' }, {queue: false});
    });
    $("#Science").mouseleave(function(){
      $('#Science').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#Arts").hover(function(){
      $('#Arts').stop().animate({ "margin-left": '62%' }, {queue: false});
    });
    $("#Arts").mouseleave(function(){
      $('#Arts').stop().animate({ "margin-left": '56%' }, {queue: false});
    });
});
