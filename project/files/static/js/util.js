

$(document).ready(function(){
    /* hide empty nav */
    if($('body>nav').html() == ''){
        $('body>nav').toggle()
    }
});