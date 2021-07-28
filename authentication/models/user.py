from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import identify_hasher
from django.contrib.auth.models import UserManager, PermissionsMixin
from utils.validators import UsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
import base64

from utils.mixins.models import SetUpModel


class User(SetUpModel, AbstractBaseUser, PermissionsMixin):

    username_validator = UsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Obrigatório, 150 caracteres ou menos. Letras, digitos e @/./+/-/ apenas.'
            ' Todos os caracteres precisam ser minúsculos.'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _("Este usuário já existe!"),
        },
    )
    name = models.CharField(_('Name'), max_length=150, blank=True)
    email = models.EmailField(_('Email adress'), blank=True, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Define if user can acess admin website'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Define if user is active'
        ),
    )

    # image = models.ImageField(blank=True, null=True)
    # image_b64 = models.TextField(null=True, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = str(self.name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name

    def image_tag(self):
        return mark_safe('<img src="data:image/png;base64, %s" width="150" height="150"/>' % self.image_b64)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        # self.image_b64 = base64.b64encode(self.image.read()) if self.image else None
        # self.image_b64 = self.image_b64.decode('utf-8')
        try:
            identify_hasher(self.password)
        except ValueError:
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
