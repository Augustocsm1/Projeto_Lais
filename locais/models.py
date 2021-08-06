from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class locais(models.Model):
    vlr_latitude = models.FloatField(_("logradouro")) 
    vlr_longitude = models.FloatField(_("bairro"))
    cod_munic = models.IntegerField(_("cidade"))
    cod_cnes = models.FloatField(_("longitude"))
    nom_estab = models.CharField(_("latitude"), max_length=255)
    dsc_bairro = models.CharField(_("nome"), max_length=255)

    def __str__(self):
        return self.dsc_bairro
