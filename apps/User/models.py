from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    id = models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        # Asegura que la contraseña esté encriptada
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username  # Mantenemos `username` como identificador