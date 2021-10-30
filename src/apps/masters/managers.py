from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Менеджер пользовательских моделей,
    в котором имя пользователя является уникальным идентификатором
    для аутентификации вместо имен пользователей.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Создайте и сохраните пользователя с заданными данными.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        extra_fields.setdefault('is_active', True)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Создайте и сохраните суперпользователя
        с указанным адресом электронной почты и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)