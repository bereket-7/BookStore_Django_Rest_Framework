from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'name', 'author', 'price']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be positive.")
        return value
