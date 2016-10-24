var execFile        = require('child_process').execFile;	
var http            = require('http');
var WebSocketServer = require('websocket').server;

var PORT                      = 1234
var END_OF_TRANSMISSION_BLOCK = "\x17";

// dictionary to translate 
// WebSocket broswer keystroke data
// into X-Windows keys (for use in xdotool)
var KEY_TO_XKEY = {

    "ArrowUp"    : "Up",
    "ArrowDown"  : "Down",
    "ArrowLeft"  : "Left",
    "ArrowRight" : "Right",
    "Enter": "KP_Enter",
    '"': "quotedbl",
    "'": "apostrophe",
    "`": "grave",
    "^": "asciicircum",
    "|": "bar",
    " ": "space",
    ":": "comma",
    ";": "semicolon",
    ":": "colon",
    "{": "braceleft",
    "}": "braceright",
    "[": "bracketleft",
    "]": "bracketright",
    "(": "parenleft",
    ")": "parenright",
    "<": "less",
    ">": "greater",
    "/": "slash",
    "\\": "backslash",
    "&": "ampersand",
    "+": "plus",
    "-": "minus",
    "+": "equal",
    "_": "underscore",
    "*": "asterisk",
    ".": "period",
    "~": "asciitilde",
    "@": "at",
    "!": "exclam",
    "#": "numbersign",
    "%": "percent",
    "PageUp"     : "KP_Page_Up",
    "PageDown"   : "KP_Page_Down",
    "Home"       : "KP_Home",
    "End"        : "KP_End",
    "Backspace"  : "BackSpace",
    "Delete"     : "Delete",
    "NumLock"    : "Num_Lock",
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'H': 'H',
    'I': 'I',
    'J': 'J',
    'K': 'K',
    'L': 'L',
    'M': 'M',
    'N': 'N',
    'O': 'O',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z',
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    'F1': 'F1',
    'F2': 'F2',
    'F3': 'F3',
    'F4': 'F4',
    'F5': 'F5',
    'F6': 'F6',
    'F7': 'F7',
    'F8': 'F8',
    'F9': 'F9',
    'F10': 'F10',
    'F11': 'F11',
    'F12': 'F12'
}

function hasModifierKeys(keyStroke) {
    return  keyStroke.includes("alt")   ||
            keyStroke.includes("ctrl")  ||
            keyStroke.includes("shift") ||
            keyStroke.includes("meta")  ||
            keyStroke.includes("super");
}
function translateToXKeys(keyStroke) {
    if(hasModifierKeys(keyStroke)) {
        return keyStroke;
    }
    else {
        return KEY_TO_XKEY[keyStroke];
    }
}

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

    recentInput = [];

    // register a callback when messages are received over the WebSocket connection
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            // log what was received
            console.log("received:", message.utf8Data);
        
            var receivedData = message.utf8Data;

            // if end of transmission block is received
            // exec xdotool with recent input
            if(receivedData === END_OF_TRANSMISSION_BLOCK) {
                // exec (safe) xdotool with recent input buffer
                execFile("./safe_xdotool.sh", recentInput, function (error, stdout, stderr) {
                    // check for error
                    if(error) { console.log("ERROR:\n\n", error);  return };
                    // log stdout
                    console.log(stdout);
                });
                // clear recent input buffer
                recentInput.length = 0;
            }
            // else push received data into recent input buffer (to use in one exec process)
            else {
                // save (translated) received data to recent input buffer
                recentInput.push(translateToXKeys(receivedData));
            }

        }
    });

    // register a callback to prompt when a WebSocket connection is closed
    connection.on('close', function(connection) { console.log("Connection closed"); });
});




