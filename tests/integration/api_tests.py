# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import unittest

from api import app


class TestsApi(unittest.TestCase):
    def __init__(self, test_name):
        super(TestsApi, self).__init__(test_name)

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_api_get_product_by_id(self):
        response = self.app.get('/products/{product_id}'.format(product_id=39))
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        expected_data = dict(
            description_text=u"Side pockets<br>Comfort flex waistband<br>Adjustable drawstring<br>For comfortable and durable sleepwear and lounge-wear in one, turn to these Hanes Men's Knit Shorts. They're also nice for relaxing around the house or doing a bit of work on your laptop. This men's sleepwear has two side pockets, an adjustable drawstring waistband and a button fly. They also have that Hanes comfort-flex fit.<br>Hanes Men's 2-Pack Knit Shorts:<br>Comfort-flex waistband<br>Cotton/Polyester shorts have a front button<br>Side pockets<br>Includes adjustable drawstring<br>Machine wash cold<br>Fabric Care Instructions: for best results, machine wash separately before wearing. Machine wash cold with like colors. Use only non-chlorine bleach when needed. Tumble dry low. Cool iron if needed<br>Fabric Content: 100% cotton (Heathers: 60% cotton/ 40% polyester)<br>Primary Color: Multi-Color<br>Multi Pack Indicator:<br>Battery Type: Does Not Contain a Battery<br>Model No.: 1005/2<br>Shipping Weight (in pounds): 1.0<br>Product in Inches (L x W x H): 6.0 x 6.0 x 1.0<br>Assembled in Country of Origin: Imported<br>Origin of Components: Imported",
            size_infos=u"[{'size_identifier': u'size-s', 'size_name': u'S', 'stock': 1}, {'size_identifier': "u"u'size-m', 'size_name': u'M', 'stock': 1}, {'size_identifier': u'size-l', 'size_name': u'L', 'stock': 1}, {'size_identifier': u'size-xl', 'size_name': u'XL', 'stock': 1}]",
            title=u"Hanes Men's 2 Pack Knit Shorts",
            url=u'http://www.walmart.com/ip/Hanes-Men-s-2-Pack-Knit-Shorts/34415953',
            discounted=0.0,
            discount=0,
            base_sku=u'34415953',
            brand=u'Hanes',
            category_names=u"Clothing,Men,Men's Sleepwear & Robes",
            image_urls=u'http://i5.walmartimages.com/dfw/dce07b8c-db0f/k2-_6d72d274-a2ba-4e5a-8d43-70073effce7d.v2.jpg',
            id=39,
            currency=u'USD',
            color_name=u'GREY HEATHER / BLACK',
            country_code=u'us',
            timestamp=u'Wed, 07 Oct 2015 01:53:46 GMT',
            current_price_value=12.96,
            original_price_value=12.96,
            identifier=u'34415953_GREYHEATHERBL',
            gender_names=u'men'
        )
        self.assertEqual(response_data, expected_data, msg=response_data)

    def test_api_get_product_by_current_price_desc(self):
        response = self.app.get('/products/current_price')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data[0]['id'], 236319)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_current_price_asc(self):
        response = self.app.get('/products/current_price?order=asc')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        response_data = sorted(response_data, key=lambda k: k['id'])
        self.assertEqual(response_data[0]['id'], 39406)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_current_price_limit(self):
        response = self.app.get('/products/current_price?limit=10')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 10)

    def test_api_get_product_by_discount_desc(self):
        response = self.app.get('/products/discount?order=desc')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        response_data = sorted(response_data, key=lambda k: k['id'])
        self.assertEqual(response_data[0]['id'], 241615)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_discount_asc(self):
        response = self.app.get('/products/discount?order=asc')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data[0]['id'], 7704)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_discount_limit(self):
        response = self.app.get('/products/discount?limit=10')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 10)

    def test_api_get_product_by_discounted_desc(self):
        response = self.app.get('/products/discounted?order=desc')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data[0]['id'], 622139)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_discounted_asc(self):
        response = self.app.get('/products/discounted?order=asc')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        response_data = sorted(response_data, key=lambda k: k['id'], reverse=False)
        self.assertEqual(response_data[0]['id'], 3092)
        self.assertEqual(len(response_data), 20)

    def test_api_get_product_by_discounted_limit(self):
        response = self.app.get('/products/discounted?limit=10')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 10)


if __name__ == '__main__':
    unittest.main()
