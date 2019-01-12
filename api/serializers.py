from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField, ModelSerializer

# from django.contrib.auth.models import User

from django.utils.timezone import now


# class UserSerializer(ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = (
#             'pk',
#             'username',
#             'first_name',
#             'last_name', 
#             'password',
#         )
#         extra_kwargs = {"password": {
            
#                 "write_only": True,    
#             }
#         }

#     def create(self, validated_data):
#         username = validated_data['username']
#         first_name = validated_data['first_name']
#         last_name = validated_data['last_name']
#         password = validated_data['password']
#         user_obj = User(username=username, first_name=first_name, last_name=last_name)
#         user_obj.set_password(password)
#         user_obj.save()
#         return validated_data