from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    # Auto-generated ID will be created by Django

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Done', 'Done'), ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_detail = models.TextField()
    task_type = models.CharField(max_length=10, choices=STATUS_CHOICES)

   