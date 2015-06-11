/**
 * Created by luoyunjiao on 2015/6/10.
 */

$(document).ready(function(){
    $('.deleteAction').click(function (e) {
        var article_id = $(e.target).closest('.article').attr('data-article-id');

        $.post(
            "delete.html",
            {
                articleId: article_id
            },
            function(data) {
                if(data == "fail") {
                    alert("Your password or adminName is not true");
                }
            }

        )

    });
});