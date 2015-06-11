/**
 * Created by luoyunjiao on 2015/6/10.
 */


$(document).ready(function(){
    $('form').submit(function () {
        var admin_name = $('.adminName input').val();
        var admin_password = $('.adminPassword input').val();

        $.post(
            "adminLogin.html",
            {
                adminName: admin_name,
                adminPassword: admin_password
            },
            function(data) {
                if(data == "fail") {
                    alert("Your password or adminName is not true");
                }
            }

        )

    });
});
