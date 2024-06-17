from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(Pago)
admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(Detalle_Producto)
admin.site.register(Proveedor)
admin.site.register(Detalle_Compra)
