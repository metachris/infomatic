import os
import logging
import subprocess as sub
import tornado.web

logger = logging.getLogger("infomatic")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.get_argument("url", None, True)
        if url:
            logger.info("load url: %s" % url)
            sub.Popen(["midori", url])
        self.write("URL: <form action='.'><input type='text' name='url' /> <input type='submit' /></form>")
