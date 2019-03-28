import unittest

import bool_test
import utils_test
import lambda_test
import int_test

from lang.expr import *

#initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()


#add test to test suite
suite.addTests(loader.loadTestsFromModule(bool_test))
suite.addTests(loader.loadTestsFromModule(utils_test))
suite.addTests(loader.loadTestsFromModule(lambda_test))
suite.addTests(loader.loadTestsFromModule(int_test))

#initialise a runner, pass it your suite
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

