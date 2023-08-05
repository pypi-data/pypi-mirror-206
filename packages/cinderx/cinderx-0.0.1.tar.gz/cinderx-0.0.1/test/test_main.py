import cinderx
import unittest


class CinderXTests(unittest.TestCase):
    def test_call_hello(self):
        self.assertIs(cinderx.hello(), None)


if __name__ == "__main__":
    unittest.main()
