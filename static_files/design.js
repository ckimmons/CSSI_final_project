$(window).load(function () {
     $('h1').fadeIn(2000).removeClass('hidden');
     $('.hexagon').fadeIn(1000).removeClass('hidden');

<<<<<<< HEAD
    $("#English").mouseenter(function(){
      $('#English').stop().animate({ "margin-left": '50%' }, {queue: false});
=======
    $("#English").hover(function(){
      $('#English').stop().animate({ "margin-left": '40%' }, {queue: false});
>>>>>>> 3c8135c4983964e5a7bdfeb7dbc1560913133d9c
    });
    $("#English").mouseleave(function(){
      $('#English').stop().animate({ "margin-left": '45%' }, {queue: false});
    });

<<<<<<< HEAD
    $("#Math").mouseenter(function(){
      $('#Math').stop().animate({ "margin-left": '65%' }, {queue: false});
=======
    $("#Math").hover(function(){
      $('#Math').stop().animate({ "margin-left": '55%' }, {queue: false});
>>>>>>> 3c8135c4983964e5a7bdfeb7dbc1560913133d9c
    });
    $("#Math").mouseleave(function(){
      $('#Math').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
<<<<<<< HEAD
    $("#Humanities").mouseenter(function(){
      $('#Humanities').stop().animate({ "margin-left": '65%' }, {queue: false});
=======
    $("#Humanities").hover(function(){
      $('#Humanities').stop().animate({ "margin-left": '55%' }, {queue: false});
>>>>>>> 3c8135c4983964e5a7bdfeb7dbc1560913133d9c
    });
    $("#Humanities").mouseleave(function(){
      $('#Humanities').stop().animate({ "margin-left": '50%' }, {queue: false});
    });
<<<<<<< HEAD
    $("#Science").mouseenter(function(){
      $('#Science').stop().animate({ "margin-left": '50%' }, {queue: false});
=======
    $("#Science").hover(function(){
      $('#Science').stop().animate({ "margin-left": '40%' }, {queue: false});
>>>>>>> 3c8135c4983964e5a7bdfeb7dbc1560913133d9c
    });
    $("#Science").mouseleave(function(){
      $('#Science').stop().animate({ "margin-left": '45%' }, {queue: false});
    });
<<<<<<< HEAD
    $("#Arts").mouseenter(function(){
      $('#Arts').stop().animate({ "margin-left": '50%' }, {queue: false});
=======
    $("#Arts").hover(function(){
      $('#Arts').stop().animate({ "margin-left": '40%' }, {queue: false});
>>>>>>> 3c8135c4983964e5a7bdfeb7dbc1560913133d9c
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
