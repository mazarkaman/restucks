from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 2}}

    def create(self, validated_data):
        email = validated_data.get('email')
        e = get_user_model().objects.filter(email=email)
        if e:
            msg = _("email is duplicated")
            raise serializers.ValidationError(msg)

        user = get_user_model().objects.create_user(**validated_data)
        return user



class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user login"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _("email or password is incorrect")
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
