from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from auth_beer.models                import User
from auth_beer.serializers import UserUpdatedSerializer


class UserUpdateView(GenericAPIView):
    """
     Updates the user due to the provided id and return the new user information.
    """
    serializer_class = UserUpdatedSerializer
    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        serializer = UserUpdatedSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)