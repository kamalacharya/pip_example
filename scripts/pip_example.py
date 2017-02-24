#!/usr/bin/env python2

import os
import sys
from subprocess import check_output, check_call

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(SCRIPT_DIR)

def main():
    print 'current dir = %s' % SCRIPT_DIR

    print "Executing bash script ../bash_scripts/get_env.sh..."
    get_env_result = check_output([SCRIPT_DIR + '/../bash_scripts/get_env.sh'])
    print get_env_result

