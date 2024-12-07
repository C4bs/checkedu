from rest_framework import serializers
from .models import Aluno, Presenca

class AlunoSerializer(serializers.ModelSerializer):
    qr_code = serializers.ImageField(read_only=True)

    class Meta:
        model = Aluno
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'
