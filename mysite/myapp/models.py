from django.db import models

# Create your models here.

class EdgeDetection(models.Model):
    name = models.CharField(default="edges", max_length=20)

    lane_perspective_floor = models.PositiveIntegerField(default=0)
    lane_perspective_roof = models.PositiveIntegerField(default=0)
    lane_perspective_startfloor = models.PositiveIntegerField(default=0)
    lane_perspective_stopfloor = models.PositiveIntegerField(default=0)
    lane_perspective_startroof = models.PositiveIntegerField(default=0)
    lane_perspective_stoproof = models.PositiveIntegerField(default=0)
    lane_left_rect_x = models.PositiveIntegerField(default=0)
    lane_left_rect_y = models.PositiveIntegerField(default=0)
    lane_left_rect_width = models.PositiveIntegerField(default=0)
    lane_left_rect_height = models.PositiveIntegerField(default=0)
    lane_right_rect_x = models.PositiveIntegerField(default=0)
    lane_right_rect_y = models.PositiveIntegerField(default=0)
    lane_right_rect_width = models.PositiveIntegerField(default=0)
    lane_right_rect_height = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name