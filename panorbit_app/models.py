from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=15)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'phone_number']

    def __str__(self):
        return self.email

class city(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30, )
    country_code = models.CharField(max_length=3)
    district = models.CharField(max_length=30)
    population = models.IntegerField()


class country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=52)
    continent = models.CharField(max_length=30)
    region = models.CharField(max_length=26)
    surface_area = models.DecimalField(max_digits=10, decimal_places=2)
    indep_year = models.IntegerField()
    population = models.IntegerField()
    life_expectancy = models.DecimalField(max_digits=3, decimal_places=1)
    gnp = models.DecimalField(max_digits=10, decimal_places=2)
    gnp_old = models.DecimalField(max_digits=10, decimal_places=2)
    local_name = models.CharField(max_length=45)
    government_name = models.CharField(max_length=45)
    head_of_state = models.CharField(max_length=60)
    capital = models.IntegerField()
    code2 = models.CharField(max_length=2)


class countrylanguage(models.Model):
    country_code = models.ForeignKey(country, primary_key=True, on_delete=models.CASCADE)
    language = models.CharField(max_length=30)
    is_official = models.CharField(max_length=1)
    percentage = models.FloatField(default=0.0)
