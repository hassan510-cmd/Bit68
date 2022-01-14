from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .serializers import UsersSerializer
from User.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from Product.api.v1.serializers import ProductSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            if user.check_password_match():
                user.save()
                token = Token.objects.create(user=user.instance)
                return Response(data={'user': user.data, 'token': token.key},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data={'message': 'confirm password not match'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(
                data={'message': user.errors},
                status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_seller_product(self):
        print(self.user)
        return Response(data=ProductSerializer(
            instance=self.user.rel_products.all(),
            many=True).data)
