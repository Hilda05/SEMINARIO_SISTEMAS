$(function($){
	var socket=io();
	$("#partida").submit(function(event) {
		
		socket.emit("partidanueva",$(this).serializeObject());
		return false;
	});
	
	socket.on("partidanueva",function(server){
		html="";
		for (var i=0;i<server.length;i++)
		{
			html+="<table border='1'><tr><td>Partidas:</td><td>"+server[i].partida+"</td></tr>";
			html+="<tr><td>Jugadores:</td><td>"+server[i]+"</td><tr>";
			html+="<tr><td>Tipo :  </td><td>"+server[i].tipo+"</td></tr>";
			html+="<tr><td>Temas: </td><td>"+server[i].categorias+"</td><tr>";
			html+="<tr><td>Numero de Preguntas :</td><td>"+server[i].entradalista+"</td><tr>";
			html+="<tr><td>Tienpo Maximo : </td><td>"+server[i].entradalista1+"</td><tr>";
			html+="<tr><td colspan='2'><input type='submit' value='Entrar'></td></tr></table>";
		}
		$("#container").html(html);
	});
});