from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.masters.managers import UserManager


class Master(AbstractUser):
    """ Master Instance """
    objects = UserManager()

    REQUIRED_FIELDS = ['password']

    SEX_CHOICES = (
        ('not_specified', _('Gender Not Specified')),
        ('male', _('Male')),
        ('female', _('Female')),
    )

    sex = models.CharField(
        _('Пол'), max_length=24,
        choices=SEX_CHOICES, default=SEX_CHOICES[0][0])
    age = models.IntegerField(
        _('Возраст'), blank=True, default=20,
        validators=[MinValueValidator(1), MaxValueValidator(120)])

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'master'
        ordering = ('username',)