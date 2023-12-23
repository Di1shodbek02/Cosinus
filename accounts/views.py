from django.contrib.auth.views import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegisterSerializer

User = get_user_model()


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        username = request.data['username']
        phone_number = request.data['phone_number']
        password = request.data['password']
        password2 = request.data['password2']
        data = request.data

        if password != password2:
            return Response({"message": "Passwords are not same!"})

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists!"}, status=400)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"message": "Phone number already exists!"}, status=400)

        try:
            avatar = data['avatar']
        except:
            data['avatar'] = None

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LogoutAPIView(APIView):
    pеrmission_classes = (IsAuthenticated,)

    def post(self, request):
        rеfresh_token = request.data.get('refresh')
        token = RefreshToken(rеfresh_token)
        token.blacklist()
        return Response(status=204)


