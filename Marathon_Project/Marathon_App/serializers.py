from os import name
from django.contrib.auth.models import User
from rest_framework import  serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from Marathon_App.models import CustomUser

User = get_user_model()    

class UserSerializer(serializers.ModelSerializer):
    
    """  serializer for User model """
    
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["groups"]
        extra_kwargs = {
            'is_superuser': {'write_only': True},
            'is_active': {'write_only': True},
            'user_permissions': {'write_only': True},           
            'password': {'write_only': True}
        }   

class TokenSerializer(serializers.ModelSerializer):
    
    """  serializer for Token model """
    
    user = serializers.SerializerMethodField('get_user')
    
    def get_user(self, obj):
        
        """ customize fields for Login API """
        
        userdata = CustomUser.objects.filter(
            id=self.instance.user.id
        ).values('id','date_of_birth')
        
        return userdata
    
    class Meta:
        model = Token
        fields = ['key','user']
    
