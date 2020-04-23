from rest_framework import serializers

from medicine_delivery.models import Medicine


class MedicineDetailsValidationSerializer(serializers.Serializer):
    get_list = serializers.BooleanField(required=True)
    medicine_name = serializers.CharField(required=False)
    price_range = serializers.CharField(required=False)
    manufacturer_slug = serializers.CharField(required=False)

class MedicineDetailsModelSerializer(serializers.ModelSerializer):
    medicine_manufacturer = serializers.SerializerMethodField()

    def get_medicine_manufacturer(self, obj):
        return obj.medicine_manufacturer.medicine_manufacturer_name

    class Meta:
        model = Medicine
        fields = ['medicine_name', 'medicine_manufacturer', 'medicine_price', 'medicine_expiry_date']


class LoginValidationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
