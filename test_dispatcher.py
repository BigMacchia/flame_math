#!/apps/Linux64/aw/maya2014-x64-sp2/bin/mayapy

import sys
import os
import unittest

current_path = os.path.abspath(__file__)
current_path = current_path.rsplit(os.sep, 1)[0]
test_path = current_path + "/tests"

if not test_path in sys.path :
	sys.path.append(test_path) 

def main():
    loader = unittest.TestLoader()
    ts = loader.discover( test_path, 'test_*.py' )

    testRunner = unittest.runner.TextTestRunner(verbosity=2)
    print ts
    #formatting 
   print "\n"
    print "----------------------------------------------------------------------"
    testRunner.run(ts)

if __name__ == "__main__" :
	main()
