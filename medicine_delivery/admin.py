from django.contrib import admin
from medicine_delivery.models import MedicineManufacturer, MedicalShop, Medicine, Order

# Register your models here.
admin.site.register(MedicalShop)
admin.site.register(MedicineManufacturer)
admin.site.register(Medicine)
admin.site.register(Order)
