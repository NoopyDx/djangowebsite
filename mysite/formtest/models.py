from django.db import models

# Create your models here.

class Mail(models.Model):
    mail = models.CharField(max_length = 200)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.mail

class Mail2(models.Model):
    mail2 = models.CharField(max_length = 200)
    name2 = models.CharField(max_length = 50)

    def __str__(self):
        return self.mail2
    


