from django.db import models

class About(models.Model):
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    idioms = models.CharField(max_length=100)
    currentJob = models.CharField(max_length=100)
    mainFormation = models.CharField(max_length=100)
    socialMedia = models.CharField(max_length=200)
    mainStack = models.CharField(max_length=100)
    problemsISolve = models.CharField(max_length=100)

    def __str__(self): 
        return self.name

class Projects(models.Model):
    TYPES = [('sites','sites'),('outros','outros')]

    projectType = models.CharField(max_length=100, choices=TYPES)
    title = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=200)
    projectLink = models.CharField(max_length=100)
    updatedAt = models.DateField()

    def __str__(self): 
        return self.title

class Achievements(models.Model):
    title = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=200)
    when = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    challenges = models.CharField(max_length=100)
    Achievements = models.CharField(max_length=100)

    def __str__(self): 
        return self.title

class Academic(models.Model):
    title = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=200)
    when = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    challenges = models.CharField(max_length=100)
    Achievements = models.CharField(max_length=100)

    def __str__(self): 
        return self.title

class Jobs(models.Model):
    title = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=200)
    when = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    challenges = models.CharField(max_length=100)
    Achievements = models.CharField(max_length=100)

    def __str__(self): 
        return self.title
