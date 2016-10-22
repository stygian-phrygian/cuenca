	
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

// create the websocket server (from the normal http server)
webSocketServer = new WebSocketServer({httpServer: server});

// WebSocket server
webSocketServer.on('request', function(request) {
    var connection = request.accept(null, request.origin);

    // This is the most important callback for us, we'll handle
    // all messages from users here.
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
	    // TODO send this shit to xdotool
            console.log(message.utf8Data);
        }
    });

    connection.on('close', function(connection) {
        // close user connection
    });

    /*
     * this breaks everything... iunno?
    connection.socket.setTimeout(3000);
    connection.socket.on('timeout', function () {
        console.log("TIMEOUT WAS EMITTED!"); 
    });
    */
    
});


