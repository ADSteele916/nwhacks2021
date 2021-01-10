from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=10)
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def get_grade(self) -> float:
        weights = 0.0
        rsf = 0.0
        for b in self.bin_set.all():
            weights += b.weight
            rsf += b.weight * b.get_grade()
        return rsf / weights * 100.0


class Bin(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    drop_n_lowest = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_grade(self) -> float:
        weighted_assignments = [(a.weight, a.get_grade() * a.weight) if a.mark is not None else (0.0, 0.0) for a in self.assessment_set.all()]
        weighted_marks = [wa[1] for wa in weighted_assignments]
        for i in range(self.drop_n_lowest):
            idx = weighted_marks.index(min(weighted_marks))
            weighted_marks.pop(idx)
            weighted_assignments.pop(idx)
        return sum(weighted_assignments)


class Assessment(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], null=True)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_grade(self) -> float:
        return self.mark / self.total
