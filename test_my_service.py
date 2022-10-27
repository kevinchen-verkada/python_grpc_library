import unittest

from myservice_grpc import my_service_pb2_grpc


def get_foo():
    return "foo"


class TestEnvironCtx(unittest.TestCase):
    def test_modified_environ__no_args(self) -> None:
        actual = get_foo()
        self.assertEqual(actual, "foo")


if __name__ == "__main__":
    unittest.main()
