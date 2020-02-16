# Command line program to convert a Shopify Customer Export file into Facebook Custom Audience List format.
#
# See, https://github.com/johntelforduk/shopify-to-facebook

import sys
import csv
# import os

# Output Facebook Custom Audience List header row.
print('email,phone,fn,ln,zip,ct,st,country,value')


facebook_writer = csv.writer(sys.stdout, lineterminator='\n')

shopify_line_num = 0                        # Current line number in Shopify file that is being processed.
for shopify_row in csv.reader(iter(sys.stdin.readline, '')):
    assert len(shopify_row) == 19           # Correctly parsed, there should always be 19 columns in each row.

    shopify_line_num += 1

    if shopify_line_num != 1:               # Omit the Shopify file Customer Export file header row.
        facebook_row = [shopify_row[2],         # email

                        # TODO Add country code to phone number.
                        shopify_row[12],        # phone

                        shopify_row[0],         # fn (First Name)
                        shopify_row[1],         # ln (Last Name)
                        shopify_row[11],        # zip (Zip/Postal Code)
                        shopify_row[6],         # ct (City)
                        shopify_row[7],         # st (State/Province)
                        shopify_row[10],        # country
                        shopify_row[14]         # value (Customer Value)
                        ]

        facebook_writer.writerow(facebook_row)
