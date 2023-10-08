from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    detail=models.CharField(max_length=1000)
    cat=models.IntegerField()
    created_at=models.DateTimeField()


    