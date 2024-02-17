from django.db import models

# Create your models here.
class New(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='epic')
    desination=models.CharField(max_length=250)

    def __str__(self):
        return self.name

