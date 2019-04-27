import unittest

import tests.bool_expr
import tests.utils
import tests.lambda_expr
import tests.int_expr
import tests.compound_expr
import tests.universal_type



#initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()


#add test to test suite
suite.addTests(loader.loadTestsFromModule(tests.bool_expr))
suite.addTests(loader.loadTestsFromModule(tests.utils))
suite.addTests(loader.loadTestsFromModule(tests.lambda_expr))
suite.addTests(loader.loadTestsFromModule(tests.int_expr))
suite.addTests(loader.loadTestsFromModule(tests.compound_expr))
suite.addTests(loader.loadTestsFromModule(tests.universal_type))

#initialise a runner, pass it your suite
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

