import requests
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


def find_region():
    ip_to_region_dict = {
        "US": "US-East"
    }

    ip_data = requests.get("https://ipinfo.io/ip", verify=False)
    ip = ip_data.text.split('\n')[0]
    geo_ip_data = requests.get("https://json.geoiplookup.io/" + ip, verify=False)
    geo_dict = geo_ip_data.json()

    return ip_to_region_dict[geo_dict["country_code"]]


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **new_params):
        """Create new user, set and save the password."""
        # pass email and any new params to new model 'user'.
        user = self.model(email=email, **new_params)
        user.set_password(password)
        # Add support for multiple databases.
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """Create new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

    def create_user_with_ip_to_aws_region(self, email, password, **new_params):
        """Create user with ip to region translation."""
        user = self.create_user(email, password, **new_params)
        user.is_staff = True
        user.region = find_region()
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model to support email only records."""
    # One-to-one relationship with emails and their users
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=63, default='NOREGION')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    # instantiate UserManager object
    objects = UserManager()

    USERNAME_FIELD = "email"
