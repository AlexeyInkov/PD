from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file", 'uploaded_at', 'processed']

    def create(self, validated_data):
        return File.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.file = validated_data.get('file', instance.file)
        instance.processed = validated_data.get('processed', instance.processed)
        instance.save()
        return instance
