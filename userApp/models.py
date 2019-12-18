from django.db import models

# Create your models here.
class AxfUser(models.Model):
    u_name = models.CharField(max_length=128)
    u_password = models.CharField(max_length=256)
    u_emial = models.CharField(max_length=64)
    u_img = models.ImageField(upload_to='icon')

    u_active = models.BooleanField(default=False)

    u_token = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_user'