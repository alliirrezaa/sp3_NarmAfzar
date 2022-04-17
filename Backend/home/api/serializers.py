from rest_framework import serializers
from ..models import *

class ContactSerializer(serializers.Serializer):
    subject=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=20)
    message=serializers.CharField(max_length=20)
    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=faq
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

