from django.contrib import admin
import products.models

admin.site.register(products.models.Customer)
admin.site.register(products.models.Product)
admin.site.register(products.models.Order)
admin.site.register(products.models.Order_item)
admin.site.register(products.models.ShippingAddress)



