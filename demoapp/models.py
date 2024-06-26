from django.db import models



class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Prefer not to say"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    dateofbirth = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False, default='default_password')
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False, unique=True)
    registrationtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "customer_table"


class Newspaper(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    Pages = models.IntegerField(blank=False)
    side_choices = (("tl", "top left"), ("tr", "top right"), ("bl", "bottom left"),("br", "bottom rigth"))
    side = models.CharField(blank=False, choices=side_choices, max_length=10)
    content = models.TextField(max_length=200, blank=False)
    image = models.FileField(blank=False, upload_to="newsimages")

    class Meta:
        db_table = "newspaper_table"

class Pomplet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    Pagecount = models.IntegerField(blank=False)
    page_choices = (("H", "horizontal"), ("V", "vertical"))
    fold = models.CharField(blank=False, choices=page_choices, max_length=10)
    content = models.TextField(max_length=200, blank=False)
    image = models.FileField(blank=False, upload_to="pompletimages")

    class Meta:
        db_table = "pomplet_table"

class Horror(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    message = models.TextField(max_length=200, blank=False)

    class Meta:
        db_table = "horror_table"

class Action(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    message = models.TextField(max_length=200, blank=False)

    class Meta:
        db_table = "action_table"

class Devotional(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    message = models.TextField(max_length=200, blank=False)

    class Meta:
        db_table = "devotional_table"

class Insta(models.Model):
    name = models.CharField(max_length=100, blank=False)
    instaid = models.EmailField(max_length=50, blank=False, unique=True)
    link = models.TextField(max_length=50, blank=False)

    class Meta:
        db_table = "insta_table"

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"