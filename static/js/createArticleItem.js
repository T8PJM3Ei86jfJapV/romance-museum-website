/**
 * Created by luoyunjiao on 2015/6/10.
 */

$(document).ready(function(){

    //获取用户名,html,type post到后台

    var ue = UE.getEditor('editor');



    $("form").submit(function(){
        var userName = $('.header .userName a').text();
        var articleHtml = UE.getEditor('editor').getAllHtml();
        var type = $('input[name="mode"]').val();
        var title = $('.titleInput input').val();
        $.post(
            //这个路径你自己补上啦
            "abc.html",
            {
                title: title,
                name: userName,
                html: articleHtml,
                mode: type

            },
            function(data) {
                if(!data) {
                    alert("你的文章尚未提交成功")
                }
            }
        )
    });
});