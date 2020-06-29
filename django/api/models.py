from django.db import models

from datetime import date

class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    created_on = models.DateField(default=date.today)
    last_updated = models.DateField(default=date.today)

    class Meta:
        db_table = 'ingredient'
        ordering = ['id']

    def __str__(self):
        return "{}: {}".format(self.name, self.description)