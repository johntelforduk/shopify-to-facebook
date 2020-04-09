# Part of, https://github.com/johntelforduk/shopify-to-facebook

from phone_codes import PhoneCode
import unittest


class TestPhoneCode(unittest.TestCase):

    def test_country_to_idd(self):
        pc = PhoneCode()
        self.assertEqual(pc.country_to_idd(country='US'), '+1')
        self.assertEqual(pc.country_to_idd(country='GB'), '+44')
        self.assertEqual(pc.country_to_idd(country='NO_SUCH_COUNTRY'), '')

    def test_enrich_phone_no(self):
        pc = PhoneCode()

        self.assertEqual('', pc.enrich_phone_no(phone_no='', country='GB'))

        tests = [('07321 432556', '', '07321 432556'),
                 ('07321 432556', 'NO_SUCH_COUNTRY', '07321 432556'),
                 ('+44 7321 452556', 'GB', '+44 7321 452556'),
                 ('0044 7321 452556', 'GB', '+44 7321 452556'),
                 ('1-234-567-8910', 'US', '1-234-567-8910'),
                 ('1-234-567-8910', 'AS', '1-234-567-8910'),            # American Samoa also has IDD code 1.
                 ('614016289999', 'AU', '614016289999'),
                 ('447321452556', 'GB', '447321452556')]

        for (test_phone_no, country, expected_result) in tests:
            self.assertEqual(expected_result, pc.enrich_phone_no(test_phone_no, country=country))


if __name__ == '__main__':
    unittest.main()
