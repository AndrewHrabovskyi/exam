import tested_progr
import unittest
import sys



class TestArr(unittest.TestCase):

    def test_basic(self):
        cases = (1,3,5)

        results = (7,11,15)

        for a, r in zip(cases, results):
            with self.subTest(case=a):
                b_r = tested_progr.main(a)
                self.assertTrue((b_r==r),msg="test_basic: a = " + str(a) + ", b_r = " + str(b_r) + ", r = " + str(r))


    def test_negative(self):
        cases = (-1,-3,-5)

        results = (3,-1,-5)

        for a, r in zip(cases, results):
            with self.subTest(case=a):
                b_r = tested_progr.main(a)
                self.assertTrue((b_r==r),msg="test_basic: a = " + str(a) + ", b_r = " + str(b_r) + ", r = " + str(r))


    def test_exceptions(self):
        cases = (2.2,[5,4],"aaaa")

        for a in cases:
            with self.subTest(case=a):
#                b = tested_progr.main(a)
                self.assertRaises(TypeError, tested_progr.main, a)


def sort_test_suite():
    suite = unittest.TestSuite()

    suite.addTest(TestArr('test_basic'))
    suite.addTest(TestArr('test_negative'))
    suite.addTest(TestArr('test_exceptions'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_suite = sort_test_suite()
    runner.run(test_suite)
