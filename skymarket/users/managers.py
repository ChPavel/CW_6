from django.contrib.auth.models import (
    BaseUserManager
)
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserRoles(models.TextChoices):
    """

    """
    USER = 'USR', _('user') # первое значение идёт в базу, второе читаемый формат (библа gettext_lazy)
    ADMIN = 'ADM', _('admin')


# Менеджер должен содержать как минимум две следующие функции
class UserManager(BaseUserManager):
    """
    Класс для создания пользователей с ролями user и admin (superuser).
    """
    def create_user(self, email, first_name, last_name, phone, role=UserRoles.USER, password=None):
        """
        Функция создания пользователя — в нее мы передаем обязательные поля
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role=UserRoles.ADMIN, password=None):
        """
        Функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )

        user.save(using=self._db)
        return user
