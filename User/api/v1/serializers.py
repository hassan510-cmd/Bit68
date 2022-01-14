from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersSerializer(ModelSerializer):
    confirm_password = CharField(max_length=225, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'confirm_password']

    def check_password_match(self):
        return self.validated_data['password'] == \
               self.validated_data['confirm_password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('username'),
                                   email=validated_data['email'],
                                   password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
