from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass #so its easy to add additional fields later on

class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) #models.SET_NULL, SET_DEFAULT if null=True of default=is set to something
    #foreign key is created in class Lead as every lead will have only one Agent. If it was defined in Agent then one agent can have only one lead.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


    """
    SOURCE_CHOICES = (
        #set a tuple
        ('YT-displayvalue','Youtube-stores in database'),
        ('Google,' 'Google'),
        ('Newsletter', 'Newsletter'),
    )
    #can override in database, only a python restriction

    #phoned = models.BooleanField(default=False)
    #source = models.CharField(choices = SOURCE_CHOICES, max_length=100)

    #profile_picture = models.ImageField(blank=True, null=True) #blank=submitting an empty string, null=no value in database (both needed for optional)
    #special_files = models.FieldFields(blank=True, null=True)
    """

    