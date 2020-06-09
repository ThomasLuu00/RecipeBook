from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.description)