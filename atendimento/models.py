from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class atendimento(models.Model):
    dsc_nome = models.CharField(_("nome"), max_length=255)
    vlr_idade = models.IntegerField(_("idade"))

    def __str__(self):
        return self.dsc_nome