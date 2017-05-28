Cuenca
======

Transmit voice recognized simulated keystrokes from a guest to host OS via browser WebSockets.

*this is a hack*

Installation
------------

*On the host:*

    npm install
    npm start    #listens on 192.168.56.1:1234 by default

*On the guest:*

    Configure your guest OS to have a named host network adaptor.

    Download client.html to your guest OS.  

Usage
-----

Open client.html in your guest OS ***then*** switch focus out of your VM into host OS applications.
