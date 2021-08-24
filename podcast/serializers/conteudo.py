from rest_framework import serializers

from podcast.models import ConteudoModel
from podcast.serializers import ArquivoSerializer


class ConteudoSerializer(serializers.ModelSerializer):
    file = ArquivoSerializer(required=False)

    class Meta:
        model = ConteudoModel
        fields = [
            "id",
            "id_conteudo",
            "title",
            "members",
            "thumbnail",
            "description",
            "published_at",
            "file",
        ]

    def create(self, validated_data):
        arquivo = validated_data.pop("file")
        file = ArquivoSerializer(data=arquivo)
        file.is_valid(raise_exception=True)
        file = file.save()
        validated_data["file_id"] = file.pk

        return super(ConteudoSerializer, self).create(validated_data)
