from django.urls import path
# from django.urls import include

from . import views
urlpatterns = [
    path('' , views.api_home)
    #path('products/', include('products.urls'))
]
