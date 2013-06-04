from django.db import models


class Website(models.Model):
    domain = models.CharField(max_length=100)
    app_id = models.BigIntegerField()
    app_secret = models.CharField(max_length=100)
    ga_id = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s (%d)" % (self.domain, self.app_id)
