from django.contrib import admin

# Register your models here.


from .models import Product
from .models import ProductCategory
from .models import Modifier
from .models import ModifierCategory

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Modifier)
admin.site.register(ModifierCategory)
