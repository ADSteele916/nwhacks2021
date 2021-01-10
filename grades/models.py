from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=10)
    credits = models.PositiveSmallIntegerField()


class Bin(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    drop_n_lowest = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Assessment(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
