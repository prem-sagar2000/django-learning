""" This file contain CustomUser that extends AbstractUser to add a new field company """
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """This CustomUser class extends AbstractUser for adding the additional fields like company"""
    company = models.CharField(max_length=100)
    