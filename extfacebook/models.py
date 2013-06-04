import json
import urllib

from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone


class ExtendedUser(models.Model):
    username = models.CharField('username', max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=90, blank=True)
    last_name = models.CharField(_('last name'), max_length=90, blank=True)
    email = models.EmailField(_('email address'), max_length=200)
    facebook_id = models.BigIntegerField()
    access_token = models.TextField()
    app_id = models.BigIntegerField(default=0, db_index=True)
    is_active = models.BooleanField(_('active'), default=True, )
    is_staff = models.BooleanField(_('superuser status'), default=False, )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), default=timezone.now)
    raw_facebook_profile = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.get_username()

    def natural_key(self):
        return ( self.get_username(), )

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_facebook_profile(self):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % self.access_token)
        return json.load(fb_profile)

    def has_perm(self, perm, obj=None):
        return self.is_staff and self.is_active

    def has_perms(self, perm_list, obj=None):
        return self.is_staff and self.is_active

    def has_module_perms(self, app_label):
        return self.is_staff and self.is_active


class FacebookFanpage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    fanpage_url = models.CharField(max_length=1000)
    is_valid = models.BooleanField(default=True)

