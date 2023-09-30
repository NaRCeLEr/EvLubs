from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

user = get_user_model()

class Profile (models.Model):
    user = models.OneToOneField(user, on_delete=models.DO_NOTHING)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    status = models.TextField(null=True, blank=True)

    city = models.CharField(max_length=255, blank=True, null=True)

    Team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, null=True, blank=True)
    Club = models.ForeignKey('Club', on_delete=models.DO_NOTHING, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('Profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username
    

class Team(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    admin = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('TeamDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Club(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    admin = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('ClubDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Category(models.Model): 
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
        

class PersonEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True, blank=True)

    creater = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='personEventCreater')
    
    users = models.ManyToManyField(Profile, blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PersonEventDetail', kwargs={'pk': self.pk})
    

class TeamEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True, blank=True)

    creater = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='teamEventCreater')

    teams = models.ManyToManyField(Team, blank=True, null=True, related_name='TeamEventsTeams')
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('TeamEventDetail', kwargs={'pk': self.pk})
