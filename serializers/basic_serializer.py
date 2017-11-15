# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BasicSerializer(object):

    @classmethod
    def serialize(cls, obj):
        raise NotImplementedError()

    @classmethod
    def serialize_full(cls, obj):
        return cls.serialize(obj)

    @classmethod
    def serialize_list(cls, obj_list, serializing_function, **kwargs):
        return [serializing_function(cur_elem, **kwargs) for cur_elem in obj_list]
