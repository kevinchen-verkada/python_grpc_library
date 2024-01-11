import unittest
# import my_service_py
from foo.bar.my_service_py_bar import foo

def get_foo():
    return "foo"


class TestEnvironCtx(unittest.TestCase):
    def test_modified_environ__no_args(self) -> None:
        # my_service_py.foo()
        foo()
        actual = get_foo()
        self.assertEqual(actual, "foo")


if __name__ == "__main__":
    unittest.main()
