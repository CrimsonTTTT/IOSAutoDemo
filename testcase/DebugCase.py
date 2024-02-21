import unittest


class DebugCase(unittest.TestCase):

    def test_debug(self):
        print("success cvx")
        self.assertEqual(1, 1, "ok,success")

    def test_debug1(self):
        self.fun(1, 2, 3)
        self.fun(1, 2)
        self.fun(1)
        self.fun(1, b_conf=2)


    def fun(self, a, b_conf=1, c=True):
        print(a, b_conf, c)
