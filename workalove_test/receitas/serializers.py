from rest_framework import serializers
from .models import Receita, Chef

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'

class ReadOnlyReceitaSerializer(serializers.ModelSerializer):
    chef = ChefSerializer()
    class Meta:
        model = Receita
        exclude = []

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        exclude = []