# Shopify to Facebook
![status](https://img.shields.io/badge/status-ready%20to%20use-green)

This command line program makes it easy to convert [Shopify Customer Lists](https://help.shopify.com/en/manual/customers/import-export-customers#export-existing-customers-to-a-csv-file) into [Facebook Custom Audiences](https://www.facebook.com/micro_site/url/?click_creative_path[0]=link&click_from_context_menu=true&country=GB&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Furl%2F%3Fhref%3D%252Fbusiness%252Fhelp%252F170456843145568%253Fhelpref%253Duf_permalink%26cmsid%3D170456843145568%26creative%3Dlink%26creative_detail%3Dpermalink%26create_type%26destination_cms_id%26orig_http_referrer%3Dhttps%253A%252F%252Fwww.facebook.com%252Fbusiness%252Fhelp%252F170456843145568%253Fid%253D2469097953376494%26search_session_id&event_type=click&last_nav_impression_id=0ETa76LbaPa2lIyib&max_percent_page_viewed=83&max_viewport_height_px=754&max_viewport_width_px=1536&orig_http_referrer=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F170456843145568%3Fid%3D2469097953376494&orig_request_uri=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F170456843145568%3Fhelpref%3Duf_permalink&primary_cmsid=170456843145568&primary_content_locale=en_GB&region=emea&scrolled=true&session_id=2JkTmiMG1irC4pgTt&site=fb4b&extra_data[view_type]=v3_initial_view&extra_data[site_section]=help&extra_data[placement]=%2Fbusiness%2Fhelp%2F170456843145568&extra_data[creative_detail]=permalink). In this way, you can create campaigns in [Facebook Ads Manager](https://www.facebook.com/business/tools/ads-manager) which are targeted to your existing Shopify customers. Alternatively, you can use your Shopify customer list as the basis for a [Lookalike Audience](https://www.facebook.com/micro_site/url/?click_creative_path[0]=link&click_from_context_menu=true&country=GB&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Furl%2F%3Fhref%3D%252Fbusiness%252Fhelp%252F744354708981227%253Fhelpref%253Duf_permalink%26cmsid%3D744354708981227%26creative%3Dlink%26creative_detail%3Dpermalink%26create_type%26destination_cms_id%26orig_http_referrer%3Dhttps%253A%252F%252Fwww.facebook.com%252Fbusiness%252Fhelp%252F744354708981227%253Fid%253D2469097953376494%26search_session_id&event_type=click&last_nav_impression_id=04Wll86M6edHqaq50&max_percent_page_viewed=75&max_viewport_height_px=754&max_viewport_width_px=1536&orig_http_referrer=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F744354708981227%3Fid%3D2469097953376494&orig_request_uri=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F744354708981227%3Fid%3D2469097953376494&primary_cmsid=744354708981227&primary_content_locale=en_GB&region=emea&scrolled=true&session_id=2JkTmiMG1irC4pgTt&site=fb4b&extra_data[view_type]=v3_initial_view&extra_data[site_section]=help&extra_data[placement]=%2Fbusiness%2Fhelp%2F744354708981227&extra_data[creative_detail]=permalink).

#### Usage

The program expects to read a Shopify Customer List from `stdin`. It outputs a Facebook Custom Audiences file to `stdout`. Example usage is,

```buildoutcfg
python shop_to_face.py < examples\fictitious_shopify_export.csv > examples\fictitious_facebook_import.csv
```

#### Exporting Shopify Customer Lists

In Shopify, begin by selecting the **Customers** option in the Shopify menu, 

![Screenshot](https://github.com/johntelforduk/shopify-to-facebook/blob/master/screenshots/Shopify_menu.JPG)

Next, select the customers that you want to include in the list. In order to meet data protection laws, you should only include customers who have agreed to **Accept Marketing**.

![Screenshot](https://github.com/johntelforduk/shopify-to-facebook/blob/master/screenshots/Shopify_export.JPG)

Finally, export the customer list,

![Screenshot](https://github.com/johntelforduk/shopify-to-facebook/blob/master/screenshots/Shopify_customer_export.JPG)

#### Notice

This project uses the International Dialing Code data provided by https://github.com/siliconchild/International-Dialing-Codes

#### Disclaimers
All example data files in this project contain fictitious data.

In order to comply with the data protection laws in your country, you should only include customers who have explicitly agreed to data-driven marketing. See Facebook's [GDPR microsite](https://www.facebook.com/business/gdpr) for more information.