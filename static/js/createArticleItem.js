/**
 * Created by luoyunjiao on 2015/6/10.
 */

$(document).ready(function(){

    //获取用户名,html,type post到后台




    $(".submit").click(function(e){

        var userName = $('.header .userName a').text();
        var articleContent = $('.contentInput textarea').val();
        var encodeArticleContent = encodeURIComponent(articleContent);
        var type = $('input[name="mode"]').val();
        var title = $('.titleInput input').val();
        var encodeTitle = encodeURIComponent(title);
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
                var url = '/article/'+ data;
                redirect(url);
            }
        });



    });


     function redirect(url){
      
        top.location.href=url;//redirection
      
    }
});
