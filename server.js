var spawn           = require('child_process').spawn;	
var http            = require('http');
var WebSocketServer = require('websocket').server;

var PORT                      = 1234
var END_OF_TRANSMISSION_BLOCK = "\x17";

// spawn an initial 'xdotool' process
xdotool = spawn("xdotool", ["-"]);
xdotool.stdin.on('error', function (error) { console.log("ERROR:\n\n", error);               });
xdotool.stdin.on('exit' , function (code)  { console.log("xdotool exited with code:", code); });

// create an http server
var server = http.createServer(function(request, response) {
    // process HTTP request. Since we're writing just WebSockets server
    // we don't have to implement anything.
});
server.listen(PORT,     function () { console.log("Listening on port:",PORT);  });
server.on('connection', function () { console.log("Opened client connection..."); });
// server.maxConnection = 1; // <--- should we limit connections?

// create the websocket server (from the prior created http server)
webSocketServer = new WebSocketServer({httpServer: server});

// register a callback when a new WebSocket connection is created
webSocketServer.on('request', function(request) {
    // create a connection
    var connection = request.accept(null, request.origin);

    // register a callback when messages are received over the WebSocket connection
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            // log what was received
            console.log("received:", message.utf8Data);
        
            var receivedData = message.utf8Data;

            // if end of transmission block is received
            // end the spawned process (whereby flushing node's buffered input and executing it finally)
            if(receivedData === END_OF_TRANSMISSION_BLOCK) {
                xdotool.stdin.end();
                // spawn another process for future use
                xdotool = spawn("xdotool", ["-"]);
                xdotool.stdin.on('error', function (error) { console.log("ERROR:\n\n", error);               });
                xdotool.stdin.on('exit' , function (code)  { console.log("xdotool exited with code:", code); });
            }
            // else write to the spawned process stdin
            else {
                // make the data work with xdotool
                // data received from the WebSocket is not necessarily formatted correctly for xdotool
                receivedData = receivedData.replace("Arrow", "");
                receivedData = receivedData.replace("Enter", "KP_Return");
                receivedData = receivedData.replace(" ", "space");
        
                // write it into xdotool's stdin
                // NB. this will not trigger execution unless node's buffer is full
                xdotool.stdin.write("key " + receivedData + "\n", 'utf-8');
            }

        }
    });

    // register a callback to prompt when a WebSocket connection is closed
    connection.on('close', function(connection) { console.log("Connection closed"); });
});


