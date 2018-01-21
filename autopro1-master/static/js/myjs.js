$(function () {
    $('#automate').click(function () {
       
        var nameofauto = $('#nameofauto').val();
        var dateofauto = $('#dateofauto').val();
        $.ajax({
            url: '/api/v1.0/automate_device/ins',
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
