from django.db import models

# Create your models here.

class EdgeDetection(models.Model):
    name = models.CharField(default="edges", max_length=20)
    minVal = models.PositiveIntegerField(default=100)
    maxVal = models.PositiveIntegerField(default=100)
    pos1 = models.PositiveIntegerField(default=0)
    pos2 = models.PositiveIntegerField(default=0)
    pos3 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name