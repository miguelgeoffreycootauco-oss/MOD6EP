from django.contrib import admin

# Register your models here.
from .models import Supplier, WaterBottle, Account
admin.site.register(Supplier)
admin.site.register(WaterBottle)
admin.site.register(Account)

### All group created supplier, quantity of 5 or more, price is 1000-3000
### WaterBottle.objects.filter(supplied_by__name__in=["BF Inc.", "Abbott, Inc", "MGC Inc"], current_quantity__gte=5, cost__range=(1000, 3000))