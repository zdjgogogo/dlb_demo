#!/usr/local/bin/python
# -*- coding=utf-8 -*-

import project
import sys
import json

PNAME = sys.argv[1]
message = project.center.center(PNAME)
print json.dumps(message, sort_keys=True, indent=3)