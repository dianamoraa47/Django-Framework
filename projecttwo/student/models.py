from django.db import models
from course.models import Course

class Student(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name  = models.CharField(max_length = 50)
    Dateofbirth = models.DateField()
    Gender = models.CharField(max_length = 20)
    Registration_number = models.CharField(max_length=5)
    Email = models.EmailField(max_length = 70)
    Phonenumber  = models.CharField(max_length = 12)
    Date_joined  = models.DateField()
    Course = models.ManyToManyField(Course)
    # Image = models.ImageField(upload_to='Image',blank=True)
    

    def __str__(self):  
      return self.First_name+''+self.Last_name



    # class Post(models.Model):
    #     title = models.TextField()
    #     cover = models.ImageField(upload_to='images/')

    #     def __str__(self):
    #         return self.title

