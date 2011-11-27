$(document).ready(function() {
    $("#id_content").keydown(function(ev) {
        key = ev.keyCode
        if (!key) key = ev.charCode

        if (ev.type == 'keypress' && 115 == key && ev.ctrlKey) return false
        if (83 == key && ev.ctrlKey) {
            if (ev.type != 'keypress') $("form").submit()
            return false
        }
    });
});