# Class to do add IDD codes to phone numbers that don't have them.
# Part of, https://github.com/johntelforduk/shopify-to-facebook

import json


class PhoneCode:

    def __init__(self):

        code_file = open('International-Dialing-Codes/dialing-codes-data')
        code_json = (code_file.read())
        code_file.close()

        # Turn the JSON into a list.
        code_list = json.loads(s=code_json)

        # Turn the list into a dictionary.
        self.code_dict = {}
        for each_country in code_list:
            self.code_dict[each_country['id']] = each_country['code']

    def country_to_idd(self, country: str) -> str:
        """For parm ISO two-letter country code, return the International Direct Dailing code."""
        if country in self.code_dict:
            return self.code_dict[country]
        else:
            return ''

    def enrich_phone_no(self, phone_no: str, country: str) -> str:
        """Enrich a phone number by adding country code to front of it (if missing)."""

        # From Facebook website, https://www.facebook.com/business/help/2082575038703844?id=2469097953376494
        #
        # "Phone numbers must include a country code to be used for matching. For example, the number 1 must precede a
        # phone number in the United States. We accept up to 3 phone numbers as separate columns, with or without
        # punctuation.
        # Important: Always include the country code as part of your customers' phone numbers, even if all of your data
        # is from the same country."

        idd_code = self.country_to_idd(country)
        if idd_code == '' or phone_no == '':                    # In hopeless cases...
            return phone_no                                     # ... do nothing.

        assert len(phone_no) >= 1

        if phone_no[0] == '+':                                  # International access code present,
            return phone_no                                     # ... so no enrichment necessary.

        # Facebook give examples that start with +, but none that start with 00. So if found replace 00 with +.
        if phone_no[0:2] == '00':
            return '+' + phone_no[2:]

        # If access code is already present at start, then make no changes.
        assert idd_code[0] == '+'
        idd_code_without_plus = idd_code[1:]
        if idd_code_without_plus == phone_no[0:len(idd_code_without_plus)]:
            return phone_no
