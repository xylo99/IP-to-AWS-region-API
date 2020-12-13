from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **new_params):
        """"Create new user, set and save the password."""
        # pass email and any new params to new model 'user'.
        user = self.model(email=email, **new_params)
        user.set_password(password)
        # Add support for multiple databases.
        user.save(using=self.db)


        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model to support email only records."""
    # One-to-one relationship with emails and their users
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # instantiate UserManager object
    objects = UserManager()

    USERNAME_FIELD = 'email'
