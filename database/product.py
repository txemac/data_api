# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from sqlalchemy import Column, DateTime, Float, Integer, Text, text

import database


class Product(database.Base):
    """Product.

    :param str url: url
    :param float current_price_value: current price
    :param float original_price_value: original price
    """
    id = Column(Integer, primary_key=True)
    """Id of the product.

    An instance of :class:`sqlalchemy.types.Integer`"""

    timestamp = Column(DateTime(timezone=True), server_default=text('now()'))
    """Time the product was created.

    An instance of :class:`sqlalchemy.types.DateTime` with timezone"""

    gender_names = Column(Text)
    """Genders.

    An instance of :class:`sqlalchemy.types.Text`"""

    category_names = Column(Text)
    """Categories.

    An instance of :class:`sqlalchemy.types.Text`"""

    currency = Column(Text)
    """Currency.

    An instance of :class:`sqlalchemy.types.Text`"""

    size_infos = Column(Text)
    """Side infos.

    An instance of :class:`sqlalchemy.types.Text`"""

    country_code = Column(Text)
    """Country code.

    An instance of :class:`sqlalchemy.types.Text`"""

    title = Column(Text)
    """Title.

    An instance of :class:`sqlalchemy.types.Text`"""

    base_sku = Column(Text)
    """SKU.

    An instance of :class:`sqlalchemy.types.Text`"""

    current_price_value = Column(Float, nullable=False)
    """Current price.

    An instance of :class:`sqlalchemy.types.Float`"""

    brand = Column(Text)
    """Brand.

    An instance of :class:`sqlalchemy.types.Text`"""

    image_urls = Column(Text)
    """Url of images.

    An instance of :class:`sqlalchemy.types.Text`"""

    description_text = Column(Text)
    """Description.

    An instance of :class:`sqlalchemy.types.Text`"""

    original_price_value = Column(Float, nullable=False)
    """Original price.

    An instance of :class:`sqlalchemy.types.Float`"""

    url = Column(Text, nullable=False)
    """URL.

    An instance of :class:`sqlalchemy.types.Text`"""

    color_name = Column(Text)
    """Color.

    An instance of :class:`sqlalchemy.types.Text`"""

    identifier = Column(Text)
    """identifier.

    An instance of :class:`sqlalchemy.types.Text`"""

    __tablename__ = "product"

    def __init__(self, url, current_price_value, original_price_value):
        self.url = url
        self.current_price_value = current_price_value
        self.original_price_value = original_price_value

    @classmethod
    def create(cls, url, current_price_value, original_price_value, gender_names=None, category_names=None,
               currency=None, size_infos=None, country_code=None, title=None, base_sku=None, brand=None,
               image_urls=None, description_text=None, color_name=None, identifier=None):
        product = Product(url, current_price_value, original_price_value)
        if gender_names is not None:
            product.gender_names = gender_names
        if category_names is not None:
            product.category_names = category_names
        if currency is not None:
            product.currency = currency
        if size_infos is not None:
            product.size_infos = size_infos
        if country_code is not None:
            product.country_code = country_code
        if title is not None:
            product.title = title
        if base_sku is not None:
            product.base_sku = base_sku
        if brand is not None:
            product.brand = brand
        if image_urls is not None:
            product.image_urls = image_urls
        if description_text is not None:
            product.description_text = description_text
        if color_name is not None:
            product.color_name = color_name
        if identifier is not None:
            product.identifier = identifier

        database.session.add(product)
        database.session.commit()
        return product

    @classmethod
    def get_product_by_id(cls, product_id):
        """
        Get a product by ID.

        :param product_id: ID of the product
        :return: product
        """
        return database.session.query(cls).filter(cls.id == product_id).first()

    @classmethod
    def get_products_by_current_price(cls, limit=20, order='desc'):
        """
        Get products ordered by price.

        :param limit: limit of elements
        :param order: asc or desc
        :return: products
        """
        result = database.session.query(cls)

        if order == 'asc':
            result = result.order_by(cls.current_price_value.asc())
        else:
            result = result.order_by(cls.current_price_value.desc())

        return result.limit(limit=limit).all()

    @classmethod
    def get_products_by_discount(cls, limit=20, order='desc'):
        """
        Get products ordered by discount.
        Discount = 100 - (current_price * 100 / original_price)

        :param limit: limit of elements
        :param order: asc or desc
        :return: products
        """
        result = database.session.query(cls)

        if order == 'asc':
            result = result.order_by((100 - (cls.current_price_value * 100 / cls.original_price_value)).asc())
        else:
            result = result.order_by((100 - (cls.current_price_value * 100 / cls.original_price_value)).desc())

        return result.limit(limit=limit).all()

    @classmethod
    def get_products_by_discounted(cls, limit=20, order='desc'):
        """
        Get products ordered by discount.
        Discounted = original_price - current_price

        :param limit: limit of elements
        :param order: asc or desc
        :return: products
        """
        result = database.session.query(cls)

        if order == 'asc':
            result = result.order_by((cls.original_price_value - cls.current_price_value).asc())
        else:
            result = result.order_by((cls.original_price_value - cls.current_price_value).desc())

        return result.limit(limit=limit).all()

    @classmethod
    def get_products_by_colour(cls, colour):
        """
        Get products with a colour.

        :param colour: colour to filter
        :param limit: limit of elements
        :return: products
        """
        return database.session.query(cls).filter(cls.color_name == colour).all()
