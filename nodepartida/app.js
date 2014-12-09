var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
var users = require('./routes/users');

var app = express();
var mysql=require("./db/mysql");
var query=new mysql({host:"localhost",user:"root",password:"",database:"partida"});

var query2=new mysql(
    {host:"localhost",
    user:"root",
    password:"",
    database:"partida"});


var session=require("./session/django");
var reviewsession=session();
//llamada a socket.io
var io=require("socket.io");

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});
module.exports = app;
var nicknames=[];
var PORT=3000;
var http=app.listen(PORT,function(){
    console.log("Corriendo el puerto "+PORT);
});
var partidas=Array();
var sockets=io(http);
sockets.on("connection",function(socket){
    socket.on("mensajes",function(clientedata){
        if(clientedata.nick===socket.nickname)
        {
            sockets.sockets.emit("mensajes",clientedata);
            return;
        }
        sockets.sockets.emit("mensajes",false);
    });
    socket.on("partidanueva",function(cliente){
        partidas.push(cliente);
        socket.broadcast.emit("partidanueva",partidas)
    });
    socket.on("setnickname",function(clientedata){
        if(verificarCuenta(clientedata.nick)){
            nicknames.push(clientedata);
            socket.nickname=clientedata.nick;
            socket.emit("setnickname",{"server":true});
            return;
        }
        socket.emit("setnickname",{"server":"El nick no esta disponible"});
        return;
    });  
});
var verificarCuenta=function(ins)
{
    for(var i=0;i<nicknames.length;i++)
    {
        if(nicknames[i].nick==ins)
        {
            return false;
        }
    }
    return true;
}