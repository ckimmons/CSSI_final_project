$(window).load(function () {
     $('h1').fadeIn(2000).removeClass('hidden');
     $('.hexagon').fadeIn(1000).removeClass('hidden');

    $("#English").hover(function(){
      $('#English').stop().animate({ "margin-left": '40%' }, {queue: false});
    });
    $("#English").mouseleave(function(){
      $('#English').stop().animate({ "margin-left": '45%' }, {queue: false});
    });

    $("#Math").hover(function(){
      $('#Math').stop().animate({ "margin-left": '55%' }, {queue: false});
    });
    $("#Math").mouseleave(function(){
      $('#Math').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#Humanities").hover(function(){
      $('#Humanities').stop().animate({ "margin-left": '55%' }, {queue: false});
    });
    $("#Humanities").mouseleave(function(){
      $('#Humanities').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
    $("#Science").hover(function(){
      $('#Science').stop().animate({ "margin-left": '40%' }, {queue: false});
    });
    $("#Science").mouseleave(function(){
      $('#Science').stop().animate({ "margin-left": '45%' }, {queue: false});
    });
    $("#Arts").hover(function(){
      $('#Arts').stop().animate({ "margin-left": '40%' }, {queue: false});
    });
    $("#Arts").mouseleave(function(){
      $('#Arts').stop().animate({ "margin-left": '45%' }, {queue: false});
    });
    $(".menuButton").click(function() {
      $("#menu").stop().slideDown(500);
    });
    $("#menu").mouseleave(function() {
      $("#menu").stop().delay().slideUp(500);
    });


});
