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
