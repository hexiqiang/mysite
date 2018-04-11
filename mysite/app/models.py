from django.db import models

# Create your models here.
class nav(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    order = models.IntegerField()
    # img = models.ImageField(upload_to='download')
    def __unicode__(self):
        return self.name