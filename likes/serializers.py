# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import IntegrityError
from rest_framework import serializers

# internal:
from likes.models import Like
# -------------------------------------------------


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'created',
            'owner',
            'post',
        ]

    
def create(self, validated_data):
    try:
        return super().create(validated_data)
    except IntergrityError:
        raise serializers.validationError9({
            'detail': 'You have already liked this post'
    })