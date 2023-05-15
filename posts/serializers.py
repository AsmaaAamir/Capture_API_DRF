# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import serializers

# internal:
from posts.models import Post
from likes.models import Like
# -------------------------------------------------


class PostSerializer(serializers.ModelSerializer):
    """
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    like_count = serializers.ReadOnlyField()
    

    def validate_image(self, value):
        """
        Validation of the image being uploaded, makign sure it not to big.
        """    
        # Limiting the size of the image to 2 megabytes   
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'The image your trying to upload is too large. Max size is 2MB.')

        # Limiting the height of the image to 4096px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'The height of the image trying to upload is larger than 4096px!'
        )

        # Limiting the width of the image to 4096px
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'The width of the image trying to upload is larger than 4096px!'
        )
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None


    class Meta:
        model = Post
        fields = [
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
            'country_choices',
            'like_id',
            'comments_count',
            'like_count',
        ]
