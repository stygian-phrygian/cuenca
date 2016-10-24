#!/bin/bash

# Safely call xdotool (avoid key stroke recursion)
#
# If the window manager has focus on the guest OS client.html page
# (while server.js is running) *do_not* send xdotool simulated keystrokes.
# Doing so would feedback into server.js which would feed into client.html
# which would feed into server.js... etc.


# exit if windowclass matches "VirtualBox"

active_window_name=`xdotool getactivewindow getwindowname`

if [[ $active_window_name == *"VirtualBox"* ]]
then
  printf "window focus on VirtualBox detected...\ndropping xdotool simulated keystrokes\n"
  exit
fi

# otherwise execute xdotool with the passed in arguments
xdotool key $@


