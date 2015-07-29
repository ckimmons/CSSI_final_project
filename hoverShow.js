$(document).ready(function () {
    $(document).on('mouseenter', '.mainitemlist', function () {
        $(this).find("#englishSubList").show();
    }).on('mouseleave', '.mainitemlist', function () {
        $(this).find("#englishSubList").hide();
    });
});
