$(document).ready(function () {
var hexIdent = ["#English", "#Math", "#Science", "#Humanities", "#Arts"]
var sections = ["#englishSubList", "#mathSubList", "#scienceSubList", "#humanitiesSubList", "#artSubList"]

var subSections = ["#Writing"] //"#storyTelling", "#Literature", "#Algebra", "#Geometry", "#Calculus",
//                     "#Stats", "#lifeScience", "Chem", "Physics", "Geology", "compSci", "History", "relStudies",
//                     "Psych", "Philo", "perfArt"]

for(var i = 0; sections.length>i; i++){
    $(hexIdent[i]).mouseenter((function(notFive){
    console.log(notFive);
<<<<<<< HEAD
<<<<<<< HEAD
       return function(){
=======
       return function(){ 
>>>>>>> 6f81a0adf62872ec3321fdd892d61294731f2335
=======
       return function(){
>>>>>>> cec0232e2fad18a53c8cb09e70f673643b4ee9d6
        $(notFive).show();
       }

    })(sections[i]))

    $(hexIdent[i]).mouseleave((function(notFive){
    console.log(notFive);
<<<<<<< HEAD
<<<<<<< HEAD
       return function(){
=======
       return function(){ 
>>>>>>> 6f81a0adf62872ec3321fdd892d61294731f2335
=======
       return function(){
>>>>>>> cec0232e2fad18a53c8cb09e70f673643b4ee9d6
        $(notFive).hide();
       }

    })(sections[i]))
}

for(var i=0; subSections.length>i;i++){
    $(subSections[i]).click(function(){
        console.log("hello");

    })

}
})
