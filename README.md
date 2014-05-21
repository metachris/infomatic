pip-pi
======

Software for Picture in Picture Mode with a Raspberry Pi



Setup
-----

    Raspberry Pi setup as seen here: http://www.niteoweb.com/blog/raspberry-pi-boot-to-browser

    $ sudo apt-get update
    $ sudo apt-get upgrade

    $ sudo apt-get install python-setuptools python-dev python-pip
    $ sudo pip install tornado
    $ sudo pip install requests

    git /etc/

    Setup AVAHI

    Put software in /opt/

    sudo pip install tornado



Midori and webserver are started via `/etc/xdg/lxsession/LXDE/autostart`


Restart: `software/webserver/main.py -p 8080 -d restart`


App Ideas
---------
* Screen Invader
* Öffentliche Verkehrsmittel
