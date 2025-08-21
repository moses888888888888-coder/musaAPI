from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    level = models.IntegerField()  # e.g. 7, 8, 9

    def __str__(self):
        return f"Grade {self.level}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, through='TeachingAssignment')

    def __str__(self):
        return self.name


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    # Optional metadata fields
    lessons_per_week = models.PositiveIntegerField(default=1)
    preferred_day = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ('teacher', 'subject', 'grade')  # Prevent duplicate assignments

    def __str__(self):
        return f"{self.teacher} teaches {self.subject} in Grade {self.grade.level}"