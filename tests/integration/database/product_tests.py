# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from sqlalchemy import func

import database
from api import app
from database.product import Product


class TestsProduct(unittest.TestCase):
    def __init__(self, test_name):
        super(TestsProduct, self).__init__(test_name)

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_product_create(self):
        count1 = database.session.query(Product).count()

        new = Product.create(
            url='url',
            current_price_value=0.99,
            original_price_value=10.99
        )

        count2 = database.session.query(Product).count()
        self.assertEqual(count1 + 1, count2)

        database.session.delete(new)
        database.session.commit()
        count3 = database.session.query(Product).count()
        self.assertEqual(count1, count3)

    def test_product_read_csv_max_id(self):
        max_id = database.session.query(func.max(Product.id)).scalar()
        self.assertEqual(max_id, 699224)

    def test_product_get_products_by_price_desc(self):
        result = Product.get_products_by_current_price(order='desc')
        self.assertEqual(result[0].id, 236319)

    def test_product_get_products_by_price_asc(self):
        result = Product.get_products_by_current_price(order='asc')
        self.assertIn(result[0].id, [420528, 420179, 420623, 420171, 420449, 420531])

    def test_product_get_products_by_discount_asc(self):
        result = Product.get_products_by_discount(order='asc')
        self.assertEqual(result[0].id, 7704)

    def test_product_get_products_by_discount_desc(self):
        result = Product.get_products_by_discount(order='desc')
        self.assertEqual(result[0].id, 420179)


if __name__ == '__main__':
    unittest.main()
