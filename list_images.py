#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a remote code running service'

import os, sys, json

APP_DIR = os.path.dirname(__file__)

with open(os.path.join(APP_DIR, 'config.json'), 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)

for lang, conf in CONFIG['languages'].items():
    img = conf['image']
    print('sudo docker run -t --rm %s ls' % img)
