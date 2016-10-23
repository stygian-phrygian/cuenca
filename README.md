#Cuenca


Transmit keystrokes from a guest to host OS via your browser.

*this is a hack*

##Installation

*On the host:*


    npm install
    npm start    #listens on 192.168.56.1:1234 by default

*On the guest:*

    Configure your guest OS to have a named host network adaptor.

    Open client.html in your guest OS browser.


When the client.html ***has focus*** keystrokes are streamed into server.js and passed into xdotool.
