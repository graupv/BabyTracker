from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
