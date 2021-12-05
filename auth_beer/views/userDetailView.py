from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from auth_beer.models                import User
from auth_beer.serializers import UserSerializer


class UserDetailView(GenericAPIView):
    """
        Gets the user due to the provided id and return the user information.
    """
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)