from django.db import models
from django.contrib.auth.models import User


continents = (
    ('africa', 'Africa'),
    ('asia', 'Asia'),
    ('europe', 'Europe'),
    ('north america', 'North America'),
    ('south america', 'South America'),
    ('antarctica', 'Antarctica'),
)


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=60, verbose_name="email", unique=True)
    phone_number = models.IntegerField(unique=True)
    continent = models.CharField(max_length=250, choices=continents)

    def __str__(self):
        return self.first_name + '  |   ' + self.surname
    