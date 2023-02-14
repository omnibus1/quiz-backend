from django.db import models

# Create your models here.
class Quiz(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self):
        return self.title