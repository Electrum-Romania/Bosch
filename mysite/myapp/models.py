from django.db import models

# Create your models here.

class EdgeDetection(models.Model):
    name = models.CharField(default="edges", max_length=20)

    lane_perspective_floor = models.PositiveIntegerField(default=250)
    lane_perspective_roof = models.PositiveIntegerField(default=750)
    lane_perspective_startfloor = models.PositiveIntegerField(default=250)
    lane_perspective_stopfloor = models.PositiveIntegerField(default=750)
    lane_perspective_startroof = models.PositiveIntegerField(default=250)
    lane_perspective_stoproof = models.PositiveIntegerField(default=750)

    def __str__(self):
        return self.name