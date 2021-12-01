from rest_framework              import serializers
from auth_beer.models.user    import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'email']

    def to_representation(self, obj):    
        user    = User.objects.get(id=obj.id)
        return {
            'id'       : user.id,
            'username' : user.username,
            'email'    : user.email,
        }

class UserUpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email']