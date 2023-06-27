from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializers(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    The create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'created_at', 'owner', 'followed', 'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
