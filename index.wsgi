#-*-coding:utf-8-*-

import sys, os

root = os.path.dirname(__file__)
packages = os.path.join(root, 'packages')
sys.path.insert(0, os.path.join(packages, 'tornado-3.2.1'))
sys.path.insert(0, os.path.join(packages, 'torndb-0.2'))

import server

application = server.application