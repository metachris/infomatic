import os
import logging
import tornado.web

logger = logging.getLogger("infomatic")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
		url = self.get_argument("url", None, True)
		if url:

        self.write("URL: <form action='.'><input type='text' name='url' /> <input type='submit' /></form>")
