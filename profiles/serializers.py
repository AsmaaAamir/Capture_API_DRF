# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import serializers

# internal:
from .models import Profile
# -------------------------------------------------


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source= 'owner.username')

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'bio',
            'created_at',
            'updated_at', 
            'image',

        ]