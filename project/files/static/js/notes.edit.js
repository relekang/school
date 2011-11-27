$(document).ready(function() {
    $(window).keypress(function(event) {
        if (!(event.which == 115 && event.ctrlKey) && !(event.which == 19)) return true;
        $("form").submit();
        event.preventDefault();
        return false;

    });
});