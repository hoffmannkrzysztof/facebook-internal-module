from django.db import models
from extfacebook.models import FacebookFanpage


class Website(models.Model):
    domain = models.CharField(max_length=100)
    app_id = models.BigIntegerField()
    app_secret = models.CharField(max_length=100)
    ga_id = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    fanpage = models.ForeignKey(FacebookFanpage,null=True,blank=True)

    def __unicode__(self):
        return u"%s (%d)" % (self.domain, self.app_id)
