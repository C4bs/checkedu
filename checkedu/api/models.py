from django.db import models

class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f'Presença de {self.aluno.nome} em {self.data}'
