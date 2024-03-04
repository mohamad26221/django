from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','password','username']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            # lastname=validated_data['lastname'],
            email = validated_data['email'],
            # job = validated_data['job'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user