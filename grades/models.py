from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import Profile


class Course(models.Model):
    name = models.CharField(max_length=10)
    credits = models.PositiveSmallIntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_grade(self) -> float:
        weights = 0.0
        rsf = 0.0
        for b in self.bin_set.all():
            weights += b.weight
            rsf += b.weight * b.get_grade() / 100.0
        return rsf / weights * 100.0

    def delete(self):
        bins_list = Bin.objects.filter(course__pk=self.pk)
        for bin in bins_list:
            bin.delete()
        super(Course, self).delete()


class Bin(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveSmallIntegerField()
    drop_n_lowest = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def delete(self):
        assessments_list = Assessment.objects.filter(bin__pk=self.id)
        for assessment in assessments_list:
            assessment.delete()
        super(Bin, self).delete()

    def __str__(self):
        return self.name

    def get_grade(self) -> float:
        weighted_assignments = [(a.weight, a.get_grade() * a.weight) if a.mark is not None else (0.0, 0.0) for a in
                                self.assessment_set.all()]
        weighted_marks = [wa[1] for wa in weighted_assignments]
        for i in range(self.drop_n_lowest):
            if len(weighted_marks) == 0:
                break
            idx = weighted_marks.index(min(weighted_marks))
            weighted_marks.pop(idx)
            weighted_assignments.pop(idx)

        return sum(list(map(lambda x: x[1], weighted_assignments))) / sum(
            list(map(lambda x: x[0], weighted_assignments))) * 100.0

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
