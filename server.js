
var exec = require('child_process').exec;	
var http = require('http');
var WebSocketServer = require('websocket').server;

var PORT = 1234

// create a normal http server
var server = http.createServer(function(request, response) {
    // process HTTP request. Since we're writing just WebSockets server
    // we don't have to implement anything.
});
server.listen(PORT, function() {
    console.log("listening on port:",PORT);
});
server.on('connection', function() {
    console.log("opened client connection");
});
// server.maxConnection = 1; // <--- should we limit connections?

// create the websocket server (from the normal http server)
webSocketServer = new WebSocketServer({httpServer: server});

webSocketServer.on('request', function(request) {
    var connection = request.accept(null, request.origin);

    // This is the most important callback for us, we'll handle
    // all messages from users here.
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log("received:", message.utf8Data);
            var command = "xdotool " + message.utf8Data;
            console.log("executing:", command);
            //exec(command);
        }
    });

    connection.on('close', function(connection) {
        // close user connection
    });
});


