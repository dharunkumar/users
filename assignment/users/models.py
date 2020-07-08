from django.db import models
import pytz
# Create your models here.

class Users(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.CharField(max_length=10, primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Timezone = models.CharField(max_length=100, choices=TIMEZONES, default='UTC')

    def get_full_name(self):
        return f"{self.FirstName} {self.LastName}"

    class Meta:
        managed = True


class ActivityPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(Users, related_name='activity_periods', on_delete=models.CASCADE)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()

    class Meta:
        managed = True
