from django.db import models

# Create your models here.
class SubscribeModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "appname"
        db_table = "appname_subscribe"

    def __str__(self):
        return self.email