from django.contrib.auth.models import User
from django.db import models 

class MessCut(models.Model):
    user = models.ForeignKey(User)
    start_date = models.DateTimeField()
    end_date = models.DateField()
    days = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + str(self.start_date) + "-" + str(self.end_date)