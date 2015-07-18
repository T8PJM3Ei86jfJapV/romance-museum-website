$ = function(id){
	return document.getElementById(id);
}; 

window.onload = function(){
	createcode();
	$("checkcode").onclick = function(){createcode();}
	$("acc").onfocus = function(){objonfocus(this);}
    $("acc").onblur = function(){
    	objonblur(this);
    	isvalidAcc();
    }
    $("pass").onfocus = function(){objonfocus(this);}
    $("pass").onblur = function(){
    	objonblur(this);
    	isvalidPass();	
    }
	$("check").onfocus = function(){objonfocus(this);}
    $("check").onblur = function(){
    	objonblur(this);
		validate();
	}
}

function objonfocus(obj){
	if(obj.value=="必填")
		obj.value="";
}
function objonblur(obj){
	if(obj.value=="")
    	obj.value="必填";
}

function tipstyle(obj){
	obj.style.color = "red";
	obj.style.fontSize = "small";
}

function isvalidAcc(){
	var acc = $("acc").value;
	var validate = RegExp(/^[0-9a-zA-Z]*$/g).test(acc);
	if((acc != "必填") && (!validate || acc.length < 6 || acc.length > 32)){
		// $("acctip").innerHTML = "6-32位字母数字";
		// tipstyle($("acctip"));
	}
	else{
		$("acctip").innerHTML = "";
	}
}

function isvalidPass(){
	var pass = $("pass").value;
	if((pass != "必填") && (pass.length < 10)){
		// $("passtip").innerHTML = "长度至少为10位";
		// tipstyle($("passtip"));
	}
	else{
		$("passtip").innerHTML = "";
	}
}

function createcode(){
    code = "";
    var codeLength = 4;
    var checkcode = $("checkcode");
    var random = new Array(0,1,2,3,4,5,6,7,8,9);
    for(var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random()*10);
        code += random[index]; 
    }  
    checkcode.innerHTML = code;
}

function validate(){
	var inputCode = $("check").value;      
    if((inputCode != "必填") && (inputCode != code) ) { 
        var checktip = $("checktip");
		checktip.innerHTML = "请输入正确的验证码";
		tipstyle($("checktip")); 
        createcode();
        $("check").value = ""; 
    }         
    else{
		$("checktip").innerHTML = "";
	}        
}