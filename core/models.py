from django.db import models


class Odam(models.Model):
    name = models.CharField(max_length=222)
    fam = models.CharField(max_length=222)
    yosh = models.IntegerField()

    def __str__(self):
        return self.name