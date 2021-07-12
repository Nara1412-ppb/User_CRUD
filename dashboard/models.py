from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import logging
from django.utils import timezone
# Create your models here.
logger= logging.getLogger()
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, FirstName,LastName, EmailId, MobileNo, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not (FirstName and LastName):
            raise ValueError("The user's Name must be set")
        if not EmailId:
            raise ValueError('The given EmailId must be set')
        if not password:
            raise ValueError('The given password must be set')
        if not MobileNo:
            raise ValueError('The given mobile must be set')
        EmailId = self.normalize_email(EmailId)
        user = self.model(FirstName =FirstName, LastName =LastName ,EmailId=EmailId, MobileNo=MobileNo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, FirstName,LastName , EmailId, MobileNo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( FirstName,LastName, EmailId, MobileNo, password, **extra_fields)

    def create_superuser(self,FirstName,LastName,MobileNo, EmailId, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            logger.error('creating super user with is_staff=False.')
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            logger.error('creating super user with is_superuser=False.')
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(FirstName,LastName, EmailId, MobileNo , password, **extra_fields)
# Create your models here.
class User(AbstractUser):
    username = None
    email = None
    first_name = None
    last_name = None
    FirstName = models.CharField(max_length=25,blank = False)
    LastName = models.CharField(max_length=25,blank=False)
    EmailId = models.EmailField(max_length=250, unique=True)
    MobileNo = models.CharField(max_length=14,unique=True)
    DOB = models.DateField(default=timezone.now)
    Address = models.TextField(max_length=500)
    Gender = models.CharField(max_length=6)
    CountryId = models.IntegerField(default=0)
    CountryName = models.CharField(max_length=20)
    CityId = models.IntegerField(default=0)
    CityName = models.CharField(max_length=25)
    CreatedOn = models.DateTimeField(default=timezone.now)
    Skills = models.CharField(max_length=50)

    USERNAME_FIELD = 'EmailId'
    REQUIRED_FIELDS = ['FirstName','LastName','MobileNo']

    objects = CustomUserManager()

