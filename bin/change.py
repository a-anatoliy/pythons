#!/usr/bin/python
# -*- coding: UTF-8 -*-
    

import sys, json, argparse, logging, io, os, os.path
from pprint import pformat
from os.path import abspath, dirname, join

version = "1.0.1"

BASE_DIR = dirname(dirname(abspath(__file__)))
APP_CFG = join(BASE_DIR,'data/app-env-conv.json')
APP_LOG = join(BASE_DIR,'var/log/changer.log')

logger = logging.getLogger('newlogger')
handler = logging.FileHandler(APP_LOG)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.INFO)

def createParser ():
    # create Parser class
    parser = argparse.ArgumentParser(
        description = 'This script intended to change password of connecting to any of environments.',
        epilog = '(c) SomeBody 2019. No warranties.',
    )

    parser.add_argument ('-n', '--env', choices=['sDEV', 'sTEST', 'sENG'], 
        default='sDEV', help='The name of environment to change password', required=True)
    parser.add_argument ('-p', '--pswd', help='New password string.', required=True)

    return parser.parse_args()

if __name__ == '__main__':
    p = createParser()

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    print('New password [%s] for the env [%s]' % (p.pswd,p.env))

    # logger.info(pformat(APP_LOG))
    
    # Read JSON file
    logger.info("Reading JSON file: "+APP_CFG)
    with open(APP_CFG) as data_file:
        cfg_data = json.load(data_file)

    for node in cfg_data:
        if node == "data-backplane":
            endpoints = cfg_data['data-backplane']

    for env in endpoints:
        if env == p.env:
            endpoints[env]["password"] = p.pswd
            print(endpoints[env])

    # logger.info(pformat(cfg_data))

    # Write JSON file
    # with io.open('data.json', 'w', encoding='utf8') as outfile:
    #     str_ = json.dumps(cfg_data, indent=4, sort_keys=True,
    #                 separators=(',', ': '), ensure_ascii=False)
    #     outfile.write(to_unicode(str_))



