# Part of, https://github.com/johntelforduk/shopify-to-facebook

from phone_codes import PhoneCode
import unittest


class TestPhoneCode(unittest.TestCase):

    def test_country_to_idd(self):
        pc = PhoneCode()
        self.assertEqual(pc.country_to_idd(country='US'), '+1')
        self.assertEqual(pc.country_to_idd(country='GB'), '+44')
        self.assertEqual(pc.country_to_idd(country='NO_SUCH_COUNTRY'), '')


if __name__ == '__main__':
    unittest.main()
