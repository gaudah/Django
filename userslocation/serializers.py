from rest_framework import serializers

from userslocation.models import UsersLocation


class UserLocationsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLocation
        fields = (
            'userId',
            'latitude',
            'longitude',
            'area',
        )
        read_only_fields = ('id',)


class UserLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLocation
        fields = ('id',
                  'userId',
                  'latitude',
                  'longitude',
                  'area',
                  'createdAt',
                  'updatedAt')
        read_only_fields = ('id',)
