#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import tornado.web
import application

sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(
            os.path.dirname(
              os.path.abspath(__file__)
            ),
        )
    )
)


if __name__ == '__main__':
    app = application.Application()
    app.run()

