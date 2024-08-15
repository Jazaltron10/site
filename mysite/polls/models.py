from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=200)
    founded_date = models.IntegerField(default=2000)
    headquarters = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales = models.BigIntegerField()
    genre = models.CharField(max_length=100)
    platforms = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    awards = models.TextField()
    box_art_url = models.URLField()
    developers = models.ManyToManyField(Developer)

    def __str__(self):
        return self.title
