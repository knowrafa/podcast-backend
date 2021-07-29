from rest_framework import serializers

from podcast.models import ArquivoModel


class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArquivoModel
        fields = '__all__'
