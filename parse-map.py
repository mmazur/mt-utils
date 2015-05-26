#!/usr/bin/python3

import json
import urllib.request

mkdirs=[]
casts=[]

def dive(children, path=''):
    if path:
        mkdirs.append("mkdir -p '{}'".format(path))
    for child in children:
        if 'children' in child:
            dive(child['children'], path+child['name']+'/')
        else:
            casts.append("./fetch-cast.py '{}' '{}'".format(path, child['url']))

#with open('mtjson') as fmap:
with urllib.request.urlopen('http://www.manager-tools.com/mtjson') as fmap:
    unimap = json.loads(fmap.readall().decode('utf-8'))
    dive(unimap['children'], 'casts/')

    for line in mkdirs:
        print(line)

    print('\n\n\n')

    for line in casts:
        print(line)

