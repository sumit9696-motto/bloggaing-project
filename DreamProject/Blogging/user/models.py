from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class category(models.Model):
    cname = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to='static/category/', default="")
    cdate = models.DateField()

    def __str__(self):
        return self.cname


class profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=400)
    college = models.CharField(max_length=400)
    pic = models.ImageField(upload_to='static/profile/', default="")

    def __str__(self):
        return self.name

class blogdetail(models.Model):
    authorid= models.CharField(max_length=100)
    blogcategory= models.CharField(max_length=100)
    topic = models.CharField(max_length=50)
    description= models.CharField(max_length=600)
    attachment = models.ImageField(upload_to='static/blogattach/', default="")
    thumbnail = models.ImageField(upload_to='static/blogthumb/', default="")
    bdate = models.DateField()

