
$(document).ready(function(){

    //changeInfo reset
    $('#userInfoCancelChange').click(function(){
    	$('#userInfoForm').reset();
    })

    //changeInfo submit
    $('#userInfoForm').submit(function(){
    	debugger;
    	var isUserInfoChange = true;
    	var email = $('#email').val();
    	var qq = $('#qq').val();

    	 $.ajax({
            url: "/update",
            type: 'POST',
            data: {
                isUserInfoChange: true,
                email: email,
                qq: qq
            },
            success: function() {
                // var url = '/article/'+ data;
                redirect('/');
            }
        });

    });

    //changePassword reset
    $('#passwordCancelChang').click(function(){
    	$('#passwordForm').reset();
    })

    //changePassword submit
    $('#userInfoForm').submit(function(){
    	debugger;
    	var isUserInfoChange = false;
    	var orginalPassword = $('#orginalPassword').val();
    	var newPassword = $('#newPassword').val();
    	var password_confirm = $('#password-confirm').val();
    	// var qq = $('#qq').val();

    	if(newPassword != password_confirm) {
    		return false;
    	} else {
    		$.ajax({
	            url: "/update",
	            type: 'POST',
	            data: {
	                isUserInfoChange : false,
	                orginalPassword: orginalPassword,
	                newPassword : newPassword,
	                password_confirm: password_confirm
	            },
	            success: function() {
	                // var url = '/article/'+ data;
	                redirect('/');
	            }
        	});
    	}

    	

    });



});