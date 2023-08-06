import unittest
import logging
import typing

from pydt3 import DEVONthink3
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

class TestApplication(unittest.TestCase):
    def test_creation(self):
        app = DEVONthink3()
        self.assertIsNotNone(app)
        print(app.current_workspace)
        # Test fallback properties
        self.assertTrue(app.includeStandardAdditions)

    def test_properties(self):
        obj = DEVONthink3()
        type_ = type(obj)
        for name in dir(type_):
            try:
                if name.startswith('_'):
                    continue
                if isinstance(getattr(type_, name), property):
                    logger.info(f"Testing {obj}.{name}")
                    returned_value = getattr(obj, name)
                    returned_type = typing.get_type_hints(getattr(type_, name).fget)['return']
                    generic_origin = typing.get_origin(returned_type)
                    if generic_origin is not None and generic_origin is list:
                        generic_args = typing.get_args(returned_type)
                        assert len(generic_args) == 1, f"Expected 1 generic argument, got {len(generic_args)}"
                        self.assertTrue(all(isinstance(value, generic_args[0]) for value in returned_value), f"Expected all values of {type_}.{name} to be of type {generic_args[0]}, got {returned_value}")
                    else:
                        self.assertIsInstance(returned_value, returned_type)
            except NotImplementedError:
                continue
            

if __name__ == '__main__':
    unittest.main()