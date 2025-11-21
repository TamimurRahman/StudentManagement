from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def student_photo_path(instance,filename):
    return f'students/{instance.name}/{filename}'

class Student_Info(models.Model):
    STATUS=[
        ('active','Active'),
        ('inactive','Inactive'),
    ]

    CLASS_CHOICES = [
    ("1", "Class 1"),
    ("2", "Class 2"),
    ("3", "Class 3"),
    ("4", "Class 4"),
    ("5", "Class 5"),
    ("6", "Class 6"),
    ("7", "Class 7"),
    ("8", "Class 8"),
    ("9", "Class 9"),
    ("10", "Class 10"),]

    # CLASS_CHOICES = [(str(i), f"Class {i}") for i in range(1, 11)]
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    student_class=models.CharField(max_length=2, choices=CLASS_CHOICES)
    dob = models.DateTimeField(null=False,blank=False)
    status=models.CharField(max_length=10,choices=STATUS, default='active')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    adress=models.TextField(max_length=100)
    photo = models.ImageField(upload_to=student_photo_path,blank=True,null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - Class: {self.student_class} - Roll: {self.roll}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student_class', 'roll'],
                name='unique_roll_per_class'
            )
        ]

# 🔍 Eta Ki Kore?

# Class 1 → roll 1, roll 2, roll 3 allowed

# Class 2 → roll 1, roll 2, roll 3 allowed

# BUT Class 1 → roll 2 ei ta duto bar create korte chaile error dibe

# Class change korle same roll allowed