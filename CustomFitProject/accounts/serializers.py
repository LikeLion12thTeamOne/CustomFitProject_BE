from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password_confirm', 'first_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            # last_name 제외
        )
        return user


class UserAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age']

class UserGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['gender']

class UserDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['disease']

class UserHeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['height']

class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['weight']