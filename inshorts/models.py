from django.db import models

class Headline(models.Model):
  
  image = models.URLField(null=True, blank=True)
  url = models.TextField()

