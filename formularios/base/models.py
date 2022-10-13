from django.db import models

# Create your models here.


class Questionario(models.Model):
    titulo_questionario = models.CharField(max_length=30)


class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    Texto = adicionar o texto

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    Texto =
    numero =

class RespostaQuestionario(models.Model):
    nome_paciente = models.CharField(max_length=60)
    cpf_paciente = models.IntegerField(max_length=11)
    data_resposta = models.DateField()

class RespostaPergunta(models.Model):
    respostaquestionario = models.ForeignKey(RespostaQuestionario, )
    pergunta = models.ForeignKey(Pergunta, )
    opcao = models.ForeignKey(Opcao, )
