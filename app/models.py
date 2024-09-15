from django.db import models

class UrlModel(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return f"Short url for: {self.url} is {self.slug}"
