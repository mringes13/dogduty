from django.db import models

# Create your models here.

REPORTER_CHOICES = (
    ("Mark R.", "Mark R."),
    ("Katerina R.", "Katerina R."),
    ("Dawn R.", "Dawn R."),
    ("Maria R.", "Maria R."),
)
ACTIVITY_CHOICES = (
    ("Peed", "Peed"),
    ("Poop", "Poop"),
    ("Walk", "Walk"),
    ("Eat", "Eat"),
    ("Medicine", "Medicine"),
    ("Nothing", "Nothing"),
)
class Event(models.Model):
    reporter = models.CharField(max_length = 20, choices = REPORTER_CHOICES, default = "")
    activity = models.CharField(max_length = 20, choices = ACTIVITY_CHOICES, default = "")
    time = models.TimeField(blank=False, null=True)
    date = models.DateField(blank=False, null=True)

    def __str__(self):
        return 'At {self.time}, {self.reporter} witnessed that their pet {self.activity}'.format(self=self)
    
