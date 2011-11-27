$(document).ready(function() {
    $(window).keypress(function(event) {
        if (!(event.which == 115 && event.ctrlKey) && !(event.which == 19)) return true;
        save();
        event.preventDefault();
        return false;

    });
    function save(){
        var form = $("form");
        var data = "title=" + form.children("#id_title").attr("value") + "&content=" + form.children("#id_content").attr("value") + "&csrfmiddlewaretoken=" + $("input[name=csrfmiddlewaretoken]").attr("value");
        $.ajax({
            url: "/notes/save/" + form.attr("data-id") +  "/",
            type: "POST",
            data: data,
            success: function(msg){
                $("#ajax-feedback").fadeIn().html("Saved").delay(3000).fadeOut()
            },
            error: function(msg){
                $("#ajax-feedback").toggle().html(msg).delay(3000).fadeOut()
            }
        });
    }
});