# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver

import config.options
import handler.users

class Application(tornado.web.Application):

  def __init__(self,default_host='', transforms=None, wsgi=False, **settings):
      handlers = [
          (r'/users', handler.users.Users),
      ]
    
      tornado.web.Application.__init__(
          self,
          handlers      = handlers,
          default_host  = default_host,
          transforms    = transforms,
          wsgi          = wsgi,
          **settings
      )

  def run(self):
      server = tornado.httpserver.HTTPServer(self)
      server.bind(config.options.global_config.port)
      server.start(config.options.global_config.num_processes)
      tornado.ioloop.IOLoop.instance().start()

