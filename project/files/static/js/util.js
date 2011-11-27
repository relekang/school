

$(document).ready(function(){
    /* hide empty nav */
    if($('body>nav').html() == ''){
        $('body>nav').toggle()
    }

    function getAvailableTags(){
        $.ajax({
            url: "/notes/tags/",
            type: "GET",
            success: function(msg){
                return msg;
            }
        });
        return null;
    }
});

