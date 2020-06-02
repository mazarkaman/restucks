import django
from django.db import models
from django.db.utils import IntegrityError
from django.contrib.auth.models import AbstractBaseUser, \
    PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **extra):
        """Creates new user in database"""
        try:
            user = self.model(email=self.normalize_email(email),
                              **extra)
            user.set_password(password)
            user.save(using=self._db)
        except IntegrityError as Ex:
            raise IntegrityError("Duplicate")
        return user

    def create_superuser(self, email: str, password: str, **extra):
        user = self.create_user(email=email, password=password, **extra)
        user.is_superuser = True
        user.is_staff = True
        user.role = User.MANAGER
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER = 0
    MANAGER = 1

    ROLES_CHOICES = [
        (CUSTOMER, 'customer'),
        (MANAGER, 'manager'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    role = models.IntegerField(choices=ROLES_CHOICES, default=CUSTOMER)
    register_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    verification_sent_datetime = models.DateTimeField(null=True, default=None)
    objects = UserManager()
    USERNAME_FIELD = 'email'
