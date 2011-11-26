$(document).ready(function(){
    var id = $("article[data-type=note]").attr("data-id")
    var timestamp = $("article[data-type=note]").attr("data-timestamp")

    var timerId = setInterval(function(){
       $.ajax({
            url: "/notes/timestamp/",
            type: "POST",
            data: "note_id=" + id,
            success: function(msg){
                if(msg != timestamp){
                    window.location = "/notes/" + id + "/preview/"
                }
            }
        })
    }, 60000);
});