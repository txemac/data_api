# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from alembic.command import upgrade, downgrade
from alembic.config import Config

import database
import settings
from database.product import Product


config = Config(settings.ALEMBIC_TEST_FILE)


class TestsProduct(unittest.TestCase):
    def __init__(self, test_name):
        super(TestsProduct, self).__init__(test_name)

    def setUp(self):
        upgrade(config=config, revision='head')

    def tearDown(self):
        downgrade(config=config, revision='base')

    def test_product_create(self):
        count1 = database.session.query(Product).count()

        Product.create(
            url='url',
            current_price_value=0.99,
            original_price_value=10.99
        )

        count2 = database.session.query(Product).count()
        self.assertEqual(count1 + 1, count2)


if __name__ == '__main__':
    unittest.main()
