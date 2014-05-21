#!/usr/bin/env python
"""
Lounge Picture-in-Picture Miracle Webserver

Author: Chris Hager <chris@linuxuser.at>

License: GPLv3
"""
__version__ = "0.2.0"

import os
import sys
import signal
import socket
import traceback
import logging
import subprocess as sub

from os import getpid, remove, kill
from optparse import OptionParser
from time import sleep

import tornado.ioloop
import tornado.web
import tornado.options

from daemon import Daemon
from handlers import *

DIR_SCRIPT = os.path.dirname(os.path.realpath(__file__))
PIDFILE = os.path.join(DIR_SCRIPT, "webserver.pid")
LOGFILE = os.path.join(DIR_SCRIPT, "webserver.log")

# Setup Logging
LOGLEVEL = logging.DEBUG
logging.basicConfig(filename=LOGFILE, format='%(levelname)s | %(asctime)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("infomatic")
logger.setLevel(LOGLEVEL)

tornado.options.parse_command_line(["--log_file_prefix=%s" % LOGFILE])

# Catch SIGINT to shut the daemon down (eg. via $ kill -s SIGINT [proc-id])
def signal_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def main(port):
    try:
        logger.info("Starting Infomatic on port %s..." % port)
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()

    except SystemExit:
        logger.info("Shutting down via signal")

    except Exception as e:
        logger.exception(e)

    finally:
        logger.info("Lounge PIP miracle has stopped")


class MyDaemon(Daemon):
    def run(self):
        main(self.port)

    def set_options(self, port):
        self.port = int(port)


if __name__ == "__main__":
    usage = """usage: %prog [options] (start|stop|restart)"""
    desc = ("Lounge PIP Webserver")
    parser = OptionParser(usage=usage, description=desc)

    parser.add_option("-d", "--daemon", dest="daemon", action="store_true", help="Daemonize. -d [start|stop|restart]")
    parser.add_option("-p", "--port", dest="port", help="port (default=8888)")
    parser.add_option("-v", "--version", dest="version", action="store_true", help="Show version")

    (options, args) = parser.parse_args()

    if options.version:
        print __version__
        exit(0)

    port = options.port or 8888

    if options.daemon:
        daemon = MyDaemon(PIDFILE)
        daemon.set_options(int(port))

        if args[0] == "start":
            daemon.start()

        elif "stop" == args[0]:
            daemon.stop()

        elif "restart" == args[0]:
            daemon.restart()

    else:
        main(int(port))
