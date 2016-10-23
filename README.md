#Cuenca

Transmit voice recognized simulated keystrokes from a guest to host OS via browser WebSockets.

*this is a filthy hack*

##Installation

*On the host:*

    npm install
    npm start    #listens on 192.168.56.1:1234 by default

*On the guest:*

    Configure your guest OS to have a named host network adaptor.

    Download client.html to your guest OS.  

##Usage

Set window focus to client.html in your guest OS ***then*** switch focus out of your VM into host OS applications.

*Nota Bene* Infinite "key press" loops will occur if you maintain focus on client.html while server.js is running because xdotool emits *global* key presses.
