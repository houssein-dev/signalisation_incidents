from rest_framework import serializers
from .models import Incident , Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta :
        model  = Utilisateur
        fields = ['username' , 'email' , 'password' , 'role'] 
         
        def create(self , validated_data ):
            user =Utilisateur.objects.create_user(
                username=validated_data['username'],
                email   =validated_data.get('email'),
                password=validated_data['password'],
                role    =validated_data.get('role')
            )
            return user
        
class IncidentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Incident
        fields = '__all__'