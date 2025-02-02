from rest_framework import serializers
from .models import MenuItem
import bleach

class MenuItemSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])

        if(attrs['price']<200):
            raise serializers.ValidationError("Price can not be less than Tsh. 200")
        
        if(attrs['inventory']):
            raise serializers.ValidationError("Stock can not be negative")
        return super().validate(attrs)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

