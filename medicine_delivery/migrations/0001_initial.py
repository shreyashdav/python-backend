# Generated by Django 3.0.2 on 2020-03-14 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_slug', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=6, max_length=6, unique=True)),
                ('shop_owner_first_name', models.CharField(max_length=50)),
                ('shop_owner_last_name', models.CharField(max_length=50)),
                ('shop_address', models.CharField(max_length=200)),
                ('shop_lat_lng', models.CharField(max_length=100)),
                ('shop_pin_code', models.IntegerField(verbose_name=6)),
                ('shop_contact_no', models.IntegerField(verbose_name=15)),
                ('shop_contact_no_optional', models.IntegerField(verbose_name=15)),
                ('shop_email', models.EmailField(max_length=254)),
                ('shop_added_date', models.DateTimeField(auto_now_add=True)),
                ('shop_last_modified_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_slug', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=8, max_length=8, unique=True)),
                ('medicine_name', models.CharField(max_length=100)),
                ('medicine_expiry_date', models.DateField()),
                ('medicine_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_manufacturer_slug', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=4, max_length=4, unique=True)),
                ('medicine_manufacturer_name', models.CharField(max_length=100)),
                ('medicine_manufacturer_contact_no', models.IntegerField(verbose_name=15)),
                ('medicine_manufacturer_contact_no_optional', models.IntegerField(verbose_name=15)),
                ('medicine_manufacturer_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=10, max_length=10, unique=True)),
                ('order_amount', models.FloatField()),
                ('bill_no', models.IntegerField()),
                ('medical_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine_delivery.MedicalShop')),
                ('order_list', models.ManyToManyField(to='medicine_delivery.Medicine', verbose_name='list of medicines')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_delivery.MedicineManufacturer'),
        ),
    ]