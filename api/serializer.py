from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name','groups']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        #tomar el grupo de usuario 
        groups_data = validated_data.pop('groups')

        #creamos el usuario con los valores de la data
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser = False,#validated_data['is_superuser'],#no pedir para el post
            is_staff=False,#validated_data['is_staff'],#no pedir por el post
            is_active=True,#validated_data['is_active'],#default True
            date_joined=datetime.now()#validated_data['date_joined']#automatico
        )

        #usamos set_passwprd para encriptar la contraseña
        user.set_password(validated_data['password'])
        #agregarmos el usuario
        user.save()
        #le damos al usuario el grupo de usuario
        for group_data in groups_data:
             user.groups.add(group_data)

        return user