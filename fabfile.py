"""
You can see all commands with `$ fab -l`. Typical usages:
"""
import os
from fabric.api import run, local, cd, put, env
from fabric.operations import prompt, get

env.use_ssh_config = True

# Default hosts
if not env.hosts:
    env.hosts = ["infomatic"]


# Change to fabfile directory, to make relative paths work
DIR_SCRIPT = os.path.dirname(os.path.realpath(__file__))
os.chdir(DIR_SCRIPT)


def upload_dirty():
    """ Upload webserver and usblooper to a Raspberry """
    put("software", "/opt/infomatic/")
