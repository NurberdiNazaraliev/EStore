from rest_framework import serializers
from .models import *

class GunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gun
        fields = '__all__'

class OrderGunSerializer(serializers.ModelSerializer):
    gun = GunSerializer()

    class Meta:
        model = OrderGun
        fields = ['gun', 'quantity',]

class OrderSerializer(serializers.ModelSerializer):
    guns = OrderGunSerializer(many=True, read_only=True, source='ordergun_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'address', 'guns']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        guns_data = representation.pop('guns')
        representation['guns'] = [{'id': gun_data['gun']['id'], 'quantity': gun_data['quantity']} for gun_data in guns_data]
        return representation