from rest_framework import serializers

from .models import AlbumImagenes


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImagenes
        fields = "__all__"
