from django.db import models
from django.contrib.auth.models import User

# Create your models here


class videos(models.Model):
    video_name = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos_uploaded')

    def __str__(self):
        return self.video_name

class score(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    video_id =models.ForeignKey(videos,on_delete=models.CASCADE)
    point = models.IntegerField()


    
