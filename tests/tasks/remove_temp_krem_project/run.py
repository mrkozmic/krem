#!/bin/env python

import os
import shutil

from library.task import *

def run(path):
    path = os.path.abspath(path)
    result = rc.PASS
    # Init test project    
    
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
        except Exception:
            print("ERROR: Failed to remove " + str(path))
            result = rc.FAIL
    else:
        print("WARNING: " + path + " does not exist.")
        rc.SKIP
        
    if not result:
        print("Removed directory: " + str(path))
    return result