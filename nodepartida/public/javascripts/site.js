// $(function($) {
// 	// vemos el evento de teclado sobre el campo de texto nickname y verificamos si el usuario a presionado ENTER
// 	//y que no este vacio 
// 	var socket=io();
// 	$("#nickname").keydown(function(event) {
// 		if(event.keyCode==13 && $(this).val()!="")
// 		{
// 			//realizamos nuestra primera conneccion con el socket
// 			console.log(socket);
// 			socket.emit("setnickname",{"nick":$(this).val()});
// 		}
// 	});
// 	socket.on("getmensajes",function(response){
// 		console.log(response);
// 	})
// 	socket.on("setnickname",function(response){
// 		if(response.server===true)
// 		{
// 			//en caso de que el nick este disponible accedemos
// 			//al sistema de chat para ello llamaremos al metodo 
// 			//loadhtml que definiremos más abajo
// 			loadhtml("/saladechat/");
// 			$("#nickname").attr('disabled', 'true');

// 		}else{
// 			alert(response.server)
// 		}
// 	})
// 	var loadhtml=function(url)
// 	{
// 		$.ajax({
// 			url: url,
// 			type: 'GET',
// 			dataType: 'html',
// 			data: {},
// 		})
// 		.done(function(html) {
// 			$("#content").html(html);
// 			//habilitamos el envio de mensajes
// 			enabledchat();
// 			//habilitamos el envio de usuarios
// 			getUsers();
// 		})
// 		.fail(function() {
			
// 		})
// 		.always(function() {
			
// 		});
// 	}
// 	var setlista=function(userlist)
// 	{
// 		html="";
// 		for(var i=0;i<userlist.length;i++)
// 		{
// 			html+="<li>"+userlist[i].nick+"</li>"
// 		}
// 		$("#usuarios").html(html);
// 	}
// 	var getUsers=function()
// 	{
// 		socket.emit("get_users",{});
// 	}
// 	var enabledchat=function()
// 	{
// 		$("#menvio").keydown(function(event) {
// 			if(event.keyCode==13)
// 			{
// 				socket.emit("mensajes",{"nick":$("#nickname").val(),"msn":$(this).val()})
// 				$(this).val("");
// 			}
// 		});	
// 	}
// 	socket.on("get_users",function(response){
// 		setlista(response.lista);
// 	});
// 	socket.on("mensajes",function(response){
// 		console.log(response);
// 		$("#mensajes").append("<li>"+response.nick+">"+response.msn+"</li>")
// 	});
// });

$(function($) {
	var socket=io();
	$("#nickname").keydown(function(event) {
		if(event.keyCode==13 && $(this).val()!="")
		{
			socket.emit("setnickname",{"nick":$(this).val()});
		}
	});
	socket.on("setnickname",function(response){
		if(response.server===true)
		{
			loadhtml("/saladechat/");
			$("#nickname").attr('disabled', 'true');
		}else{
			alert(response.server)
		}
	})
	var loadhtml=function(url)
	{
		$.ajax({
			url: url,
			type: 'GET',
			dataType: 'html',
			data: {},
		})
		.done(function(html) {
			$("#content").html(html);
			enabledchat();
		})
		.fail(function() {
		
		})
		.always(function() {
			
 		});		
	}
	var enabledchat=function()
	{
		$("#menvio").keydown(function(event) {
			if(event.keyCode==13)
			{
				socket.emit("mensajes",{"nick":$("#nickname").val(),"msn":$(this).val()})
				$(this).val("");
			}
		});
	}
	socket.on("mensajes",function(response){
		console.log(response);
		$("#mensajes").append("<li>"+response.nick+">"+response.msn+"</li>")
	});
});