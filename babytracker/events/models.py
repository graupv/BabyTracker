from django.db import models
from django.utils.timezone import now

class Event(models.Model):
    datetime = models.DateTimeField(default = now)
    description = models.CharField(max_length = 200, null = False)
    baby = models.ForeignKey(
        'babies.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = False
    )

    def __str__(self):
        return f'Event\'s Baby: {self.baby}, date:{self.datetime})'