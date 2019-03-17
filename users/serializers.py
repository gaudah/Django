from rest_framework import serializers

from users.models import Users


class UsersLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username',
            'password'
        )


class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'firstName',
            'middleName',
            'lastName',
            'email',
            'mobile',
            'password',
            'isSuperuser',
            'isStaff',
            'isUser'
        )


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'firstName',
            'middleName',
            'lastName',
            'mobile'
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'username',
            'firstName',
            'middleName',
            'lastName',
            'email',
            'mobile',
            'password',
            'isSuperuser',
            'isStaff',
            'isUser',
            'isActive',
            'dateJoined',
            'lastLogin',
            'createdAt',
            'updatedAt'
        )
        read_only_fields = ('id',)
