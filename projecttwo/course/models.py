from django.db import models
from teacher.models import Teacher

class Course(models.Model):
	Name = models.CharField(max_length=50)
	Duration = models.CharField(max_length = 15)
	Months = models.CharField(max_length = 10)
	Startdate = models.DateField(max_length = 20)
	Enddate = models.DateField(max_length = 20)
	Description = models.TextField(max_length=150)
	Teacher = models.ForeignKey(Teacher,null = True, on_delete=models.CASCADE)

	
# Create your models here.


