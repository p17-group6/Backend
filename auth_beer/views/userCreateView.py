from rest_framework                          import status
from rest_framework.generics import GenericAPIView
from rest_framework.response                 import Response

from auth_beer.serializers.userSerializer import UserSerializer


class UserCreateView(GenericAPIView):
    """
        Create a user account with username, email and password and return the user information.
    """
    serializer_class= UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)