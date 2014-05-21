import os
import logging
import subprocess as sub

import tornado.web
import requests

SLACKOMATIC_IP = "10.20.30.90"


logger = logging.getLogger("infomatic")


def slackomatic_call_api(uri):
    """
    Translates an api-uri eg. `/device/nec/pip/size/large` into
    http://<SLACKOMATOC_IP/slackomatic/device/nec/pip/size/large
    """
    url = "http://%s/slackomatic/%s" % (SLACKOMATIC_IP, uri.lstrip("/"))
    logger.info("slackomatic api call: %s" % url)
    return requests.get(url)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.get_argument("url", None, True)
        if url:
            logger.info("load url: %s" % url)
            sub.Popen(["midori", "-e", "TabCloseOther"])
            sub.Popen(["midori", url])
        self.write("""<p><form action='.'>URL: <input type='text' name='url' /> <input type='submit' value="Open URL" /></form></p>
<hr><ul>
    <li><a href="/slackomatic">Slackomatic Control</a></li>
</ul>""")


class EnablePipHandler(tornado.web.RequestHandler):
    def get(self):
        slackomatic_call_api("/device/nec/pip/on")
        slackomatic_call_api("/device/nec/pip/size/large")


class BookmarkletHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.get_argument("url", None, True)
        if url:
            logger.info("bookmarklet url: %s" % url)
            sub.Popen(["midori", "-e", "TabNew"])
            sub.Popen(["midori", "-e", "TabCloseOther"])
            sub.Popen(["midori", url])
            slackomatic_call_api("/device/nec/pip/on")
            slackomatic_call_api("/device/nec/pip/size/large")
        self.write("""<html><head></head><script type="text/javascript">window.close();</script><body></body></html>""")


class SlackomaticHandler(tornado.web.RequestHandler):
    # http://10.20.30.90/slackomatic/layout/
    def get(self):
        slackomatic_api_call = self.get_argument("do", None, True)
        if slackomatic_api_call:
            slackomatic_call_api(slackomatic_api_call)
            self.redirect("/slackomatic")
        self.write("""<p><a href="/">Index</a></p>Slackomatic Control: <ul>
    <li><a href="/slackomatic?do=/device/nec/pip/on">PIP On</a></li>
    <li><a href="/slackomatic?do=/device/nec/pip/off">PIP Off</a></li>
    <li><a href="/slackomatic?do=/device/nec/pip/size/small">PIP Small</a></li>
    <li><a href="/slackomatic?do=/device/nec/pip/size/medium">PIP Medium</a></li>
    <li><a href="/slackomatic?do=/device/nec/pip/size/large">PIP Large</a></li>
</ul>""")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/bookmarklet", BookmarkletHandler),
    (r"/enable_pip", EnablePipHandler),  # Just opens this url in midori
    (r"/slackomatic", SlackomaticHandler),  # Runs as app
])
