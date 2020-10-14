from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Group(models Model):
    group_name = models.CharField(max_length=50)
    group_description = models.CharField(max_length=300)
    members = models.ManyToManyField(User)

class Task(models Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=300)
    estimated_duration = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    estimated_effort = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    actual_duration = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    actual_effort = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    originator = models.OneToOneField(User, on_delete=models.CASCADE)
    assignee = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    # first item is value set in model and second is human readible format
    TASK_TYPE_CHOICES = (
        ("Design","Design"),
        ("Build","Build"),
        ("Test","Test"),
        ("Review","Review")
    )

    task_type = models.CharField(max_length=25,choices=TASK_TYPE_CHOICES,default='1')
    predecessors = models.ManyToManyField('self',symmetrical=False,blank=True)
    sucessors = models.ManyToManyField('self',symmetrical=False,blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    history = HistoricalRecords() # from simple-history application. Tracks every change to Task
    
    def __str__(self):
        return self.name


