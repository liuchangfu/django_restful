# _*_ coding:utf-8 _*_
from api.models import User, Group
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
