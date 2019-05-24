from django.db import models

from .enums import StatusEnum


class Question(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    question = models.TextField(max_length=200, blank=False)
    answer = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=[(s.name, s.value) for s in StatusEnum], default=StatusEnum.P.value, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.name} asked {self.question}"

        return f"{self.get_status_display()}"




