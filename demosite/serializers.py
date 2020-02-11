from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password2'},write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','password','password2', 'email', 'first_name', 'last_name')
        # write_only_fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            
        )
        password = validated_data['password'],
        password2 = validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not matching'})
        user.set_password(password)
        user.save()
        return user