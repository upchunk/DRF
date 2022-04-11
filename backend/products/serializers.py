from itertools import product
from rest_framework import serializers

from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        # obj.user -> user.username
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, product):
            return None
        
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        