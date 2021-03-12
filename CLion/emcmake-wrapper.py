#!/usr/bin/env python3

import argparse
import os
from sys import argv

EMCMAKE = ""  # put full path here
CMAKE = ""  # put full path here


params = argv[1:]
params.insert(0, CMAKE)

parser = argparse.ArgumentParser()
parser.add_argument("--build", default=argparse.SUPPRESS)
args, unknown = parser.parse_known_args()
if 'build' in args:
    os.execv(CMAKE, params)
else:
    params.insert(0, EMCMAKE)
    os.execv(EMCMAKE, params)
