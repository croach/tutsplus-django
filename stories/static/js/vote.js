$(document).ready(function() {

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function vote (storyID) {
    debugger;
    $.ajax({
        type: "POST",
        url: "/vote/",
        data: {"story": storyID},
        success: function() {
            $("#story-vote-" + storyID).hide();
            $("#story-title-" + storyID).css({"margin-left": "15px"});
        },
        headers: {
            'X-CSRFToken': csrftoken
        }
    });
    return false;
}

$("a.vote").click(function() {
    var storyID = parseInt(this.id.split("-")[2]);
    return vote(storyID);
});

});
