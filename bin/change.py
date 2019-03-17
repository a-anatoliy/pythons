#!/usr/bin/python
# -*- coding: UTF-8 -*-
    
import sys
import json
import argparse
    
version = "1.0.1"
    

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

    print('New password [%s] for the env [%s]' % (p.pswd,p.env))
    




