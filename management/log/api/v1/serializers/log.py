from rest_framework import serializers

from management.log.models import LogModel


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogModel
        fields = '__all__'
