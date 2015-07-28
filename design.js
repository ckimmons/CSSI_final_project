$(window).load(function () {

    $(".hexagon").hover(function(){
      $('.hexagon').stop().animate({ "margin-left": '46%' }, {queue: false});
    });
          $(".hexagon").mouseleave(function(){
            $('.hexagon').stop().animate({ "margin-left": '50%' }, {queue: false});
          });
              $(".hexagon2").hover(function(){
                $('.hexagon2').stop().animate({ "margin-left": '60%' }, {queue: false});
              });
                    $(".hexagon2").mouseleave(function(){
                      $('.hexagon2').stop().animate({ "margin-left": '56%' }, {queue: false});
                    });
                        $(".hexagon3").hover(function(){
                          $('.hexagon3').stop().animate({ "margin-left": '45%' }, {queue: false});
                        });
                              $(".hexagon3").mouseleave(function(){
                                $('.hexagon3').stop().animate({ "margin-left": '49%' }, {queue: false});
                                });
                                  $(".hexagon4").hover(function(){
                                    $('.hexagon4').stop().animate({ "margin-left": '39%' }, {queue: false});
                                  });
                                        $(".hexagon4").mouseleave(function(){
                                          $('.hexagon4').stop().animate({ "margin-left": '43%' }, {queue: false});
                                          });


});
