import qrcode
from rest_framework import viewsets
from .models import Aluno, Presenca
from .serializers import AlunoSerializer, PresencaSerializer
from django.core.files.base import BytesIO
from django.core.files import File
from django.db import models

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def perform_create(self, serializer):
        aluno = serializer.save()
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(aluno.matricula)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        aluno.qr_code.save(f'{aluno.matricula}_qr.png', File(buffer), save=True)

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer
