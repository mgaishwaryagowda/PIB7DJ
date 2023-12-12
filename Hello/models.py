from django.db import models

# Create your models here.
class students(models.Model):
    student_ID=models.IntegerField()
    student_name=models.CharField(max_length=50)
    course= models.CharField(max_length=30)
    jdate=models.DateField()
    def _str_(self):
        return self.student_name
