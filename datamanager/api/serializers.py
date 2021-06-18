from rest_framework import serializers
from .models import Fruit, Provider, Bundle

#########
#  OLD  #
#########

# class FruitSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     origin = serializers.CharField(max_length=100)
#     provider = serializers.ForeignKey(Provider, on_delete=models.CASCADE)

#     def create(self, validated_data) :
#         return Fruit.objects.create(validated_data)
    
#     def update(self, instance, validated_data) :
#         instance.stock = validated_data.get('stock', instance.stock)
#         return instance

# class ProviderSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     location = serializers.CharField(max_length=100)

#     def create(self, validated_data) :
#         return Provider.objects.create(validated_data)

#########

class FruitSerializer(serializers.ModelSerializer):
    class Meta :
        model = Fruit
        fields = [ "name", "origin", "provider" ]

class ProviderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Provider
        fields = [ "name", "location" ]