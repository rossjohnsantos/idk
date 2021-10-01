from rest_framwork import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'FirstName', 'LastName', 'Email', 'password', 'created_at', 'updated_at')