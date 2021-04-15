from django.db import models
from django.db.models.signals import post_save #after commit to the database #pre_save, before commit to database
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    #so its easy to add additional fields later on
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False) #additional user properties added


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

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
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#signals, for communicating events
def post_user_created_signal(sender, instance, created, **kwargs):
    if created: #if a new user is created then execute this and create a new user profile
        UserProfile.objects.create(user=instance)
    
#name of the function to be called, the model that is going to send the event
post_save.connect(post_user_created_signal, sender=User)


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

