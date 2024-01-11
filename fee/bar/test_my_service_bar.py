import unittest

# import my_service_py
from fee.bar.my_service_py_bar import fee


def get_fee():
    return "fee"


class TestEnvironCtx(unittest.TestCase):
    def test_modified_environ__no_args(self) -> None:
        # my_service_py.fee()
        fee()
        actual = get_fee()
        self.assertEqual(actual, "fee")


if __name__ == "__main__":
    unittest.main()
