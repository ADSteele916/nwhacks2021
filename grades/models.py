from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=10)
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Bin(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    drop_n_lowest = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], null=True)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name