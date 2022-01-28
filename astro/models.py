from django.db import models

# Create your models here.
class Event(models.Model):
    Event_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=500)
    Discription=models.TextField()
    imgUrls=models.TextField()
    Info=models.TextField()
    Highlights=models.TextField()
    R1=models.TextField(default="")
    R2=models.TextField(default="")
    


    def __str__(self):
        return self.Name