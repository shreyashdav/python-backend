from django.db import models
from randomslugfield import RandomSlugField
from django.contrib.auth.models import User


class MedicalShop(models.Model):
    shop_slug = RandomSlugField(length=6)
    user_id = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100, default='')
    shop_owner_first_name = models.CharField(max_length=50)
    shop_owner_last_name = models.CharField(max_length=50, null=True, blank=True)
    shop_address = models.CharField(max_length=200)
    shop_lat_lng = models.CharField(max_length=100)
    shop_pin_code = models.IntegerField()
    shop_contact_no = models.BigIntegerField()
    shop_contact_no_optional = models.BigIntegerField(null=True, blank=True)
    shop_email = models.EmailField(null=True, blank=True)
    # shop_password = models.CharField(max_length=50)
    shop_added_date = models.DateTimeField(editable=True, auto_now_add=True)
    shop_last_modified_date = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = 'Medical Shop'

    def __str__(self):
        return 'ShopName: ' + self.shop_name + ' | ' + 'ShopAddress: ' +str(self.shop_address) + ' | ' + \
               'ShopContact: ' + str(self.shop_contact_no) + ' | ' + 'MedicalShopSlug: ' + str(self.shop_slug)


class MedicineManufacturer(models.Model):
    medicine_manufacturer_slug = RandomSlugField(length=4)
    medicine_manufacturer_name = models.CharField(max_length=100)
    medicine_manufacturer_contact_no = models.BigIntegerField(verbose_name='Contact')
    medicine_manufacturer_contact_no_optional = models.BigIntegerField('Optional Contact', null=True, blank=True)
    medicine_manufacturer_address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Medical Manufacturer'

    def __str__(self):
        return 'ManufacturerName: ' + self.medicine_manufacturer_name + ' | ' + 'ManufacturerAddress: ' + str(
            self.medicine_manufacturer_address) + ' | ' + 'ManufacturerContact: ' + \
               str(self.medicine_manufacturer_contact_no) + ' | ' + 'MedicineManufacturerSlug: ' + \
               str(self.medicine_manufacturer_slug)


class Medicine(models.Model):
    medicine_slug = RandomSlugField(length=8)
    medicine_name = models.CharField(max_length=

                                     100)
    medicine_manufacturer = models.ForeignKey(MedicineManufacturer, on_delete=models.CASCADE, null=True, blank=True)
    medicine_expiry_date = models.DateField()
    medicine_price = models.FloatField()

    def save(self, *args, **kwargs):
        self.medicine_price = round(self.medicine_price, 2)
        super(Medicine, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Medicine'

    def __str__(self):
        return 'MedicineName: ' + str(self.medicine_name) + ' | ' + 'MedicineManufacturer: ' + str(
            self.medicine_manufacturer.medicine_manufacturer_name) + ' | ' + 'MedicinePrice: ' + str(
            self.medicine_price) + ' | ' + 'MedicineSlug: ' + str(self.medicine_slug)


class Order(models.Model):
    order_id = RandomSlugField(length=10)
    medical_shop = models.ForeignKey(MedicalShop, on_delete=models.CASCADE)
    order_amount = models.FloatField()
    order_list = models.ManyToManyField(Medicine, verbose_name="list of medicines", blank=True)
    bill_no = models.IntegerField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.order_amount = round(self.order_amount, 2)
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Order'

    def __str__(self):
        return 'OrderShop: ' + self.medical_shop.shop_name + ' | ' + 'OrderAmount: ' +str(self.order_amount) + ' | ' + \
               'OrderDateTime: ' + str(self.order_date)

