import json
#from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

"""DRF Serializers Version"""
@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializers(instance).data
    return Response(data)



# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#     return Response(data)


    """Django JSON View"""
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     # model instance (model_data)
    #     # serialization
    #     # return JSON to my client
    # return JsonResponse(data)

    """Basic Python View"""
    # print(request.GET)
    # print(request.POST)
    # body = request.body
    # print(body)
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # #print(data.keys())
    # print(data)
    
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type

    # return JsonResponse(data)