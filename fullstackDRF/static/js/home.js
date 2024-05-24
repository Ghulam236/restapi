console.log("bbbbbbbbb");
$(document).ready(function() {
    $('#signupForm').submit(function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "signup",
            data: formData,
            success: function(response) {
                console.log("rrrrr",response.requestData);
                // alert(response.message);
            },
            error: function(xhr, status, error) {
                alert("Error: " + xhr.responseText);
            }
        });
    });
});