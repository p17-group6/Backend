from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auth_beer.models                import User
from auth_beer.serializers import UserSerializer

class UserDeleteView(GenericAPIView):
    """
     Delete the user due to the provided id and return no content.
    """
    permission_classes = (IsAuthenticated,)    
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)