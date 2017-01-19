# -*- coding: utf-8 -*-
import unittest
from validator import Regex_helpers

pattern = """(GIR\s0AA) |^
    (
        # A9 or A99 prefix
        ( ([A-PR-UWYZ][0-9][0-9]?) |
             # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
             # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )
            )
          )
          # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}
        )$"""
regex_helper = Regex_helpers(pattern)


class Test_validator(unittest.TestCase):
    def test_junk(self):
        self.assertEqual(regex_helper.match_string('$%±()()'), None)

    def test_invalid(self):
        self.assertEqual(regex_helper.match_string('XX XXX'), None)

    def test_incorrect_inward_code_length(self):
        self.assertEqual(regex_helper.match_string('A1 9A'), None)

    def test_no_space(self):
        self.assertEqual(regex_helper.match_string('LS44PL'), None)

    def test_q_in_first_position(self):
        self.assertEqual(regex_helper.match_string('Q1A 9AA'), None)

    def test_v_in_first_position(self):
        self.assertEqual(regex_helper.match_string('V1A 9AA'), None)

    def test_x_in_first_position(self):
        self.assertEqual(regex_helper.match_string('X1A 9BB'), None)

    def test_i_in_second_position(self):
        self.assertEqual(regex_helper.match_string('LI10 3QP'), None)

    def test_j_in_second_position(self):
        self.assertEqual(regex_helper.match_string('LJ10 3QP'), None)

    def test_z_in_second_position(self):
        self.assertEqual(regex_helper.match_string('LZ10 3QP'), None)

    def test_q_in_third_position_with_a9a_structure(self):
        self.assertEqual(regex_helper.match_string('A9Q 9AA'), None)

    def test_c_in_fourth_position_with_aa9a_structure(self):
        self.assertEqual(regex_helper.match_string('AA9C 9AA'), None)

    def test_area_with_only_single_digit_districts(self):
        self.assertEqual(regex_helper.match_string('FY10 4PL'), None)

    def test_area_with_only_double_digit_districts(self):
        self.assertEqual(regex_helper.match_string('SO1 4QQ'), None)

    def test_valid_postcodes(self):
        self.assertNotEqual(regex_helper.match_string('EC1A 1BB'), None)
        self.assertNotEqual(regex_helper.match_string('W1A 0AX'), None)
        self.assertNotEqual(regex_helper.match_string('M1 1AE'), None)
        self.assertNotEqual(regex_helper.match_string('B33 8TH'), None)
        self.assertNotEqual(regex_helper.match_string('CR2 6XH'), None)
        self.assertNotEqual(regex_helper.match_string('DN55 1PT'), None)
        self.assertNotEqual(regex_helper.match_string('GIR 0AA'), None)
        self.assertNotEqual(regex_helper.match_string('SO10 9AA'), None)
        self.assertNotEqual(regex_helper.match_string('FY9 9AA'), None)
        self.assertNotEqual(regex_helper.match_string('WC1A 9AA'), None)


if __name__ == '__main__':
    unittest.main()
