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

 
    def validate_image(self, value):
    """
    Validation of the image being uploaded.
    """
    # Limiting the size of the image to 2 megabytes   
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationsError(
                'The image your trying to upload is too large. Max size is 2MB.')

    # Limiting the height of the image to 4096 px
        if value
        return value





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
            'category_choices',
        ]
