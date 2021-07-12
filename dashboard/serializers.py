
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User  = get_user_model()

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','FirstName','LastName','EmailId','MobileNo','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(FirstName = validated_data['FirstName'],LastName = validated_data['LastName'],
                                        EmailId = validated_data['EmailId'],MobileNo = validated_data['MobileNo'],password = validated_data['password'])
        return user


    

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','FirstName','LastName','DOB', 'Address', 'Gender','CountryName','CityName','Skills')
        extra_kwargs = {'id': {'read_only': True}}
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.FirstName = validated_data.get('FirstName', instance.FirstName)
        instance.LastName = validated_data.get('LastName', instance.LastName)
        instance.DOB = validated_data.get('DOB', instance.DOB)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.Gender = validated_data.get('Gender', instance.Gender)
        instance.CountryName = validated_data.get('CountryName', instance.CountryName)
        instance.CityName = validated_data.get('CityName', instance.CityName)
        instance.Skills = validated_data.get('Skills', instance.Skills)
        instance.save()
        return instance

