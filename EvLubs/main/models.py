from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Profile (models.Model):
    user = models.OneToOneField(user, on_delete=models.DO_NOTHING)
    email = models.EmailField(blank=true, null=true)
    logo = models.ImageField(blank=true, null=true)
    status = models.TextField(null=True, blank=True)

    team = models.ForeignKey(team, on_delete=models.DO_NOTHING, blank=True, null=True)
    club = models.ForeignKey(club, on_delete=models.DO_NOTHING, blank=True, null=True)


class Team(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=true, null=true)
    description = models.TextField(null=True, blank=True)

    admin = models.OneToOneField(profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Club(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=true, null=true)
    description = models.TextField(null=True, blank=True)

    admin = models.OneToOneField(profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Category(models.Model): 
    title = models.CharField(255)

    def __str__(self):
        return self.title

class PersonEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=true, null=true)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    address = models.CharField(max_length=500, null=True, blank=True)
    
    users = models.ManyToManyField(Profile)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    

class TeamEvent(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(blank=true, null=true)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    address = models.CharField(max_length=500, null=True, blank=True)

    teams = models.ManyToManyField(Team)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
