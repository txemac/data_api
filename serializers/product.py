# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from serializers.basic_serializer import BasicSerializer


class ProductSerializer(BasicSerializer):
    @classmethod
    def serialize(cls, product):
        if product is None:
            return None
        return dict(
            id=product.id,
            current_price_value=product.current_price_value,
            original_price_value=product.original_price_value,
            url=product.url
        )

    @classmethod
    def serialize_full(cls, product):
        if product is None:
            return None

        discount = 0
        if product.current_price_value != product.original_price_value:
            discount = (100 - (product.current_price_value * 100 / product.original_price_value))

        result = cls.serialize(product)
        result.update(
            gender_names=product.gender_names,
            category_names=product.category_names,
            currency=product.currency,
            size_infos=product.size_infos,
            country_code=product.country_code,
            title=product.title,
            base_sku=product.base_sku,
            timestamp=product.timestamp,
            brand=product.brand,
            image_urls=product.image_urls,
            description_text=product.description_text,
            color_name=product.color_name,
            identifier=product.identifier,
            discount=discount,
            discounted=product.original_price_value - product.current_price_value
        )
        return result
