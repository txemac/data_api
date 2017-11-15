# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import Flask, request

from database.product import Product
from serializers.product import ProductSerializer
from server import generate_get

app = Flask(__name__)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.get_product_by_id(product_id=product_id)
    return generate_get(obj=ProductSerializer.serialize_full(product=product))


@app.route('/products/current_price', methods=['GET'])
def get_products_by_current_price():
    args = request.args
    limit = int(args.get('limit', 20))
    order = args.get('order', 'desc')

    products = Product.get_products_by_current_price(limit, order)

    return generate_get(obj=ProductSerializer.serialize_list(
        obj_list=products,
        serializing_function=ProductSerializer.serialize_full
    ))


@app.route('/products/discount', methods=['GET'])
def get_products_by_discount():
    args = request.args
    limit = int(args.get('limit', 20))
    order = args.get('order', 'desc')

    products = Product.get_products_by_discount(limit, order)

    return generate_get(obj=ProductSerializer.serialize_list(
        obj_list=products,
        serializing_function=ProductSerializer.serialize_full
    ))


@app.route('/products/discounted', methods=['GET'])
def get_products_by_discounted():
    args = request.args
    limit = int(args.get('limit', 20))
    order = args.get('order', 'desc')

    products = Product.get_products_by_discounted(limit, order)

    return generate_get(obj=ProductSerializer.serialize_list(
        obj_list=products,
        serializing_function=ProductSerializer.serialize_full
    ))


if __name__ == '__main__':
    app.run()
