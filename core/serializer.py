#from .models import AuthUser
#from django.contrib.auth.models import User
#from rest_framework import serializers
#
#class AuthUserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = AuthUser 
#        fields = '__all__'
#
#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = AuthUser
#        fields = '__all__'
#        write_only_fields = ('password',)
#        read_only_fields = ('id',)
#
#    def create(self, validated_data):
#        user = User.objects.create(
#            username=validated_data['username'],
#            email=validated_data['email'],
#            first_name=validated_data['first_name'],
#            last_name=validated_data['last_name'],
#            is_superuser = False,#validated_data['is_superuser'],#no pedir para el post
#            is_staff=validated_data['is_staff'],#no pedir por el post
#            is_active=validated_data['is_active'],#default True
#            date_joined=validated_data['date_joined']#automatico
#        )
#
#        user.set_password(validated_data['password'])
#        user.save()
#
#        return user