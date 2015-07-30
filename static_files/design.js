$(window).load(function () {

    $("#English").mouseenter(function(){
      $('#English').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#English").mouseleave(function(){
      $('#English').stop().animate({ "margin-left": '55%' }, {queue: false});
    });

    $("#Math").mouseenter(function(){
      $('#Math').stop().animate({ "margin-left": '65%' }, {queue: false});
    });
    $("#Math").mouseleave(function(){
      $('#Math').stop().animate({ "margin-left": '60%' }, {queue: false});
    });
    $("#Humanities").mouseenter(function(){
      $('#Humanities').stop().animate({ "margin-left": '65%' }, {queue: false});
    });
    $("#Humanities").mouseleave(function(){
      $('#Humanities').stop().animate({ "margin-left": '60%' }, {queue: false});
    });
    $("#Science").mouseenter(function(){
      $('#Science').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#Science").mouseleave(function(){
      $('#Science').stop().animate({ "margin-left": '55%' }, {queue: false});
    });
    $("#Arts").mouseenter(function(){
      $('#Arts').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#Arts").mouseleave(function(){
      $('#Arts').stop().animate({ "margin-left": '55%' }, {queue: false});
    });
    $(".menuButton").click(function() {
      $("#menu").stop().slideDown(500);
    });
    $("#menu").mouseleave(function() {
      $("#menu").stop().delay().slideUp(500);
    });


});
