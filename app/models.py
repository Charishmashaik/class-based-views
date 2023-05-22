from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


class student(models.Model):
    school=models.ForeignKey(school,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    def __str__(self) -> str:
        return self.sname
