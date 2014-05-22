#!/bin/bash
# Turn pip off in 25 seconds
PIDFILE="/tmp/pip_off.pid"

if [ -f $PIDFILE ]; then
  echo "killing old instance"
  kill $( cat $PIDFILE )
  rm $PIDFILE
fi

echo "$$" > $PIDFILE
echo "Sleep, then turn pip off"

cd /tmp
sleep 25
wget http://127.0.0.1:8080/slackomatic?do=/device/nec/pip/off
