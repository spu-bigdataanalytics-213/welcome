from types import ModuleType
import unittest
import importlib
import inspect


class TestMyCode(unittest.TestCase):
    """
    Test module `my_code.py` on below criteria:

    - Module is importable.
    - Module has at least two functions.
    """

    def test_import_module(self):
        try:
            user_mudule = importlib.import_module('my_code')
        except:
            self.fail('Loading module `my_code.py` failed.')

        self.assertEqual(type(user_mudule), ModuleType, msg='Not a module.')

    def test_number_of_functions(self):
        user_mudule = importlib.import_module('my_code')
        callables = inspect.getmembers(user_mudule, inspect.isfunction)

        self.assertGreater(len(callables), 1,
                           msg='Not enough functions! Make some more!')