
// var hexIdent = ["#English", "#Math", "#Science", "#Humanities", "#Arts"]
var sections = ["#englishSubList", "#mathSubList", "#scienceSubList", "#humanitiesSubList", "#artSubList"]

// var subSections = ["#Writing", "#storyTelling", "#Literature", "#Algebra", "#Geometry", "#Calculus",
//                     "#Stats", "#lifeScience", "Chem", "Physics", "Geology", "compSci", "History", "relStudies",
//                     "Psych", "Philo", "perfArt"]
    $('#English').click(function(){
        $(this).css({'display':'list-item'});
        $('#English').unbind('mouseenter mouseleave')
    }



// for(var i = 0; sections.length>i; i++){
//     $(hexIdent[i]).mouseenter((function(notFive){
//     console.log(notFive);
//
//        return function(){
//         $(notFive).show();
//
//        }
//
//     })(sections[i]))
//



  // // for(var i = 0; sections.length>i; i++){
  //     $('.English-Menu').mouseenter(
  //         function() {
  //         $('#englishSubList').show()}
  //       );
  //
  //     $('#englishSubList').mouseenter(
  //         function () {
  //         $('#subSections').show()}
  //       );



//     $(hexIdent[i]).mouseleave((function(notFive){
//     console.log(notFive);
//
//        return function(){
//         $(notFive).hide();
//        }
//
//     })(sections[i]))
// }

// for(var i=0; subSections.length>i;i++){
//     $(subSections[i]).click(function(){
//         console.log("hello");
//
//     })
//
// }
