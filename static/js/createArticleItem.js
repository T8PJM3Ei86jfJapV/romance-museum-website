/**
 * Created by luoyunjiao on 2015/6/10.
 */

$(document).ready(function(){

    //��ȡ�û���,html,type post����̨




    $(".submit").click(function(e){

        var userName = $('.header .userName a').text();
        var articleContent = $('.contentInput textarea').val();
        var type = $('input[name="mode"]').val();
        var title = $('.titleInput input').val();
        $.ajax({
            url: "/createArticle",
            type: 'POST',
            data: {
                title: title,
                name: userName,
                html: articleContent,
                mode: type
            },
            success: function(data) {
                window.location = "/article/" + data;
            }
        });



    });
});
