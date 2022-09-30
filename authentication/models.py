from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,  password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email,  password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_active') is not True:
            raise ValueError('Superuser must be active')
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **kwargs)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email



# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
# # Create your models here.


# class CustomUserManager(BaseUserManager):
#     def create_user(self,email,password,**extra_fields):
#         if not email:
#             raise ValueError(_('Please enter an email address'))

#         email=self.normalize_email(email)

#         new_user=self.model(email=email,**extra_fields)

#         new_user.set_password(password)

#         new_user.save()

#         return new_user


#     def create_superuser(self,email,password,**extra_fields):

#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_active',True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True'))

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True'))


#         return self.create_user(email,password,**extra_fields)


# class User(AbstractUser):
#     username=models.CharField(_('Username'), max_length=40,unique=True)
#     email=models.CharField(_('Email'), max_length=80,unique=True)
#     phone_number=PhoneNumberField(unique=True,null=False,blank=False)
#     date_joined=models.DateTimeField(_('Date'),auto_now_add=True)


#     REQUIRED_FIELDS=['username','phone_number']
#     USERNAME_FIELD='email'

#     def __str__(self):
#         return f"User {self.username}"

