# -*- coding: utf-8 -*-

import os
import sys

import tornado.httpclient
import tornado.options

tornado.options.define("environment", default='dev', type=str, help="Production environment <'dev', 'test', 'prod'>")
tornado.options.define("mongo_conf", type=dict, help="mongo config")
tornado.options.define("port", type=int, help="Port number used for http connection")
tornado.options.define("num_processes", type=int, help="number of processes")

def parse_command_line():
      tornado.options.parse_command_line()

def parse_config_file(config_file):
      tornado.options.parse_config_file(
          os.path.join(
              os.path.dirname(__file__),'..', config_file
          )       
      )       


parse_config_file('dolphin.conf')

global_config = tornado.options.options

