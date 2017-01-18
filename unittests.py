import unittest
import ValidatePostcodeCSV
pattern = '(GIR\s0AA)|^((([A-PR-UWYZ][0-9][0-9]?)|(([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9])|([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9])|x(WC[0-9][A-Z])|(([A-PR-UWYZ][0-9][A-HJKPSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))))\s[0-9][ABD-HJLNP-UW-Z]{2})'
regex_helper = ValidatePostcodeCSV.RegexHelper(pattern)
class test1(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='$%± ()()'), None)
class test2(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='XX XXX'), None)
class test3(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='A1 9A'), None)
class test4(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='LS44PL'), None)
class test5(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='Q1A 9AA'), None)
class test6(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='V1A 9AA'), None)
class test7(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='X1A 9BB'), None)
class test8(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='LI10 3QP'), None)
class test9(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='LJ10 3QP'), None)
class test10(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='LZ10 3QP'), None)
class test11(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='A9Q 9AA'), None)
class test12(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='AA9C 9AA'), None)
class test13(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='FY10 4PL'), None)
class test14(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='SO1 4QQ'), None)
class test15(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='EC1A 1BB'), None)
class test16(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='W1A 0AX'), None)
class test17(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='M1 1AE'), None)
class test18(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='B33 8TH'), None)
class test19(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='CR2 6XH'), None)
class test20(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='DN55 1PT'), None)
class test21(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='GIR 0AA'), None)
class test22(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='SO10 9AA'), None)
class test23(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='FY9 9AA'), None)
class test24(unittest.TestCase):
    def test(self):
        self.assertNotEqual(regex_helper.match_string( string='WC1A 9AA'), None)
if __name__ == '__main__':
    unittest.main()
