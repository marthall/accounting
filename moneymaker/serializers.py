from rest_framework import serializers
from models import Outcome, Product, OutcomeCategory


class OutcomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outcome
        fields = ('product', 'description', 'date', 'price')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category')


class OutcomeCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutcomeCategory
        fields = ('name',)
