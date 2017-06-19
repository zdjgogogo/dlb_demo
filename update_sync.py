#!/usr/local/bin/python
# -*- coding=utf-8 -*-

import project
import sys
import json

PNAME = sys.argv[1]
NAME = PNAME.split('-')
class_name = NAME[0].split('_')

if class_name[-1] == 'center':
    message = project.center.update(PNAME)
    print json.dumps(message, sort_keys=True, indent=3)
elif class_name[-1] == 'webview':
    message = project.h5.update(PNAME)
    print json.dumps(message, sort_keys=True, indent=3)
elif class_name[-1] == 'component':
    message = project.component.update(PNAME)
    print json.dumps(message, sort_keys=True, indent=3)
