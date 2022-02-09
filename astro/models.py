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

class Blog(models.Model):
    Blog_id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=500)
    Author=models.CharField(max_length=500, default="")
    Date=models.CharField(max_length=500,default="")
    headimg=models.TextField()
    Discription=models.TextField()
    Content=models.TextField()
  
    R1=models.TextField(default="")
    R2=models.TextField(default="")
    


    def __str__(self):
        return self.Title

class Profile(models.Model):
    memb_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=500)
    branch_year_mobilenumber_email_por=models.TextField()
    About=models.TextField()
    Intrests=models.TextField()
    Activities=models.TextField()
    git_lin_insta_fb=models.TextField()
    img=models.TextField()
    old=models.TextField()
  
    R1=models.TextField(default="")
    R2=models.TextField(default="")
    


    def __str__(self):
        return self.Name
class AllowedPerson(models.Model):
    auth_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=500)
    Email=models.TextField()
  

    def __str__(self):
        return self.Name
class Publication(models.Model):
    publication_id=models.AutoField(primary_key=True)
    Name=models.TextField()
    About=models.TextField()
    Thumbnail_link=models.TextField()
    Link=models.TextField()
  

    def __str__(self):
        return self.Name


class Interview(models.Model):
    interview_id=models.AutoField(primary_key=True)
    Title=models.TextField()
    Interviewee=models.TextField()
    Disc=models.TextField()
    Thumbnail=models.TextField()
    Video=models.TextField()
  

    Link=models.TextField(default="")

    def __str__(self):
        return self.Interviewee


class Photo(models.Model):
    Photo_id=models.AutoField(primary_key=True)
    Group=models.TextField()
    Link=models.TextField()
   
  


    # def __str__(self):
    #     return self.Photo_id

