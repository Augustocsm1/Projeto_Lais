from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class cidadao(models.Model):
    dsc_nome = models.CharField(_("nome completo"), max_length=255)
    dsc_nascimento = models.DateField(_("nascimento"))
    dsc_email = models.EmailField(_("email"))
    dsc_senha = models.CharField(_("senha"), max_length=50)
    dsc_senha_confirm = models.CharField(_("confirmar senha"), max_length=50)

    def __str__(self):
        return self.dsc_nome
