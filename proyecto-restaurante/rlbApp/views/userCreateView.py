from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rlbApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        userData = {
            'username':request.data['username'],
            'password':request.data['password']
                    }

        token = TokenObtainPairSerializer(data=userData)
        token.is_valid(raise_exception=True)

        return Response(token.validated_data, status=status.HTTP_201_CREATED)