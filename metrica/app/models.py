from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'Team: {self.name}'


class Person(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=15, blank=False)
    email = models.CharField(max_length=50, blank=False)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return f'Person: {self.name}'


class Metric(models.Model):
    name = models.CharField(max_length=100)
    indicator_type = models.CharField(max_length=100, blank=False)
    indicator_value = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return f'Metric: {self.name}'
