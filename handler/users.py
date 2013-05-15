# -*- coding: utf-8 -*-

import bson
import tornado.web

import handler

class Users(tornado.web.RequestHandler):

  def get(self):
    self.write("Welcome to Tornado")
