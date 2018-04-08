from django.contrib import admin
from .models import User,Category, Product,Transaction, Payment

# Register your models here.

admin.site.register(Payment)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Transaction)
