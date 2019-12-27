from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializers, GroupSerializers


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users,ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
       Return a group instance.

   list:
       Return all groups,ordered by most recently joined.

   create:
       Create a new group.

   delete:
       Remove an existing group.

   partial_update:
       Update one or more fields on an existing group.


    update:
       Update a user.

    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
