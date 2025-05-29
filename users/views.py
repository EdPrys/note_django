from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .serializers import RegisterSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Надсилання email
            send_mail(
                subject="Реєстрація в Note Project",
                message="Ви успішно зареєструвались у Note Project!",
                from_email=None,  # використає DEFAULT_FROM_EMAIL
                recipient_list=[user.email],
            )

            return Response({"message": "Користувача створено, лист надіслано."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)