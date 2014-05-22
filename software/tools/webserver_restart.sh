#!/bin/bash
export DISPLAY=:0
if [[ ! -f /opt/infomatic/software/webserver/webserver.pid ]]; then
  # not found
  echo "start"
  /opt/infomatic/software/webserver/main.py -p 8080 -d start
else
  echo "restart"
  /opt/infomatic/software/webserver/main.py -p 8080 -d restart
fi
