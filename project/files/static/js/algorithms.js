$(document).ready(function(){
    $(".algorithms li h2").click(function(){
        var details = $(this).siblings(".details");
        if(details.is(":visible")){
            details.slideUp();
        } else {
            details.slideDown();
        }
    });
});