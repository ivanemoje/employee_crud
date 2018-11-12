from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Song(models.Model):
    genre_choices = (
        ('IT', 'IT'),
        ('Legal', 'Legal'),
        ('Finance', 'Finance'),
        ('Engineering', 'Engineering'),
        ('HR', 'HR'),
    )
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=25, choices=genre_choices, default='IT')
    email = models.EmailField(blank=True, default="")
    nationality = models.CharField(max_length=25,blank=True)

    def __unicode__(self):
        return self.title 

class Profile(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    address = models.TextField()

    def __unicode__(self):
        return self.user 

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# DateField must be set to NULL 
# reason : https://stackoverflow.com/questions/48297071/sqlite-not-null-constraint-failed