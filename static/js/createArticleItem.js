/**
 * Created by luoyunjiao on 2015/6/10.
 */

$(document).ready(function(){

    //��ȡ�û���,html,type post����̨

    var ue = UE.getEditor('editor');



    $("form").submit(function(){
        var userName = $('.header .userName a').text();
        var articleHtml = UE.getEditor('editor').getAllHtml();
        var type = $('input[name="mode"]').val();
        var title = $('.titleInput input').val();
        $.post(
            //���·�����Լ�������
            "abc.html",
            {
                title: title,
                name: userName,
                html: articleHtml,
                mode: type

            },
            function(data) {
                if(!data) {
                    alert("���������δ�ύ�ɹ�")
                }
            }
        )
    });
});