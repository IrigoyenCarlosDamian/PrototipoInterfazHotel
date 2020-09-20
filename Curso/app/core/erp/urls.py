from django.urls import path
from core.erp.views import category_list
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'erp'

urlpatterns = [
    url(r'^categroy/list', category_list, name='vista1'),

]