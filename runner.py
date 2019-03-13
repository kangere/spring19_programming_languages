import unittest

import bool_test
import utils_test

#initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()


#add test to test suite
suite.addTests(loader.loadTestsFromModule(bool_test))
suite.addTests(loader.loadTestsFromModule(utils_test))

#initialise a runner, pass it your suite

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)