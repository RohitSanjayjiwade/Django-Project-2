from django.urls import path
from . import views

urlpatterns = [
    # Your URL patterns go here
    path('', views.index, name='index'),
    path('product/<int:id>', views.product_modifiers, name='product_modifiers')
]