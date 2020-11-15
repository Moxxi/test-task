from django.db import models


class Polls(models.Model):
    Name = models.CharField(max_length=200)
    DateStart = models.CharField(max_length=20)
    DateEnd = models.CharField(max_length=20)
    Description = models.CharField(max_length=300)


class Questions(models.Model):
    Poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    Option = models.CharField(max_length=200)

    TextChoice = 'TX'
    OneChoice = 'OC'
    ManyChoice = 'MC'
    TypeChoices = [
        (TextChoice, 'Text'),
        (OneChoice, 'OneChoice'),
        (ManyChoice, 'ManyChoice')
    ]

    Type = models.CharField(
        max_length=2,
        choices=TypeChoices,
        default=Text,
    )


class Answers(models.Model):
    Question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    UserId = models.IntegerField()
    Answer = models.CharField(max_length=200)


