# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import serializers

# internal:
from .models import Post

# -------------------------------------------------


class PostSerializer(serializers.ModelSerializer):
    """
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_onwer = serializers.SerializerMethodFiel()
    profile_id = serializers.ReadOnlyField(source='owner.profile.is')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Post
        field = [
            'id',
            'owner',
            'title',
            'category',
            'description',
            'created_at',
            'updated_at',
            'is_owner',
            'profile_id',
            'profile_image',
            'image',
        ]
