from django.urls import path
from .views import index, test
urlpatterns = [
    path('', index, name='ent'),
    path('test/', test, name='test'),
]
