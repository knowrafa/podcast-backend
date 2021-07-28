from rest_framework import serializers

from podcast.models import ConteudoModel


class ConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoModel
        fields = '__all__'
