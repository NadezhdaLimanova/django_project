from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='phones/')
    release_date = models.DateField(auto_now=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)


