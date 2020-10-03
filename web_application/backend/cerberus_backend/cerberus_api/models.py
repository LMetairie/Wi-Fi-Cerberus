from django.db import models
from datetime import datetime


# Données colectées
class DetectedDevices(models.Model):
    class Meta:
        ordering=['date']
        
    # Date de collection
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date de la capture')
    # TODO Ajouter un validateur pour verifier le format de l'adresse MAC.
    mac_address = models.TextField(max_length=20, unique=False, blank=False, verbose_name='Adresse MAC')
    signal_strength = models.IntegerField(blank=True, verbose_name='Puissance du signal')
    #TODO Turn off null and blank while in production.
    lat = models.FloatField(verbose_name='Latitude', blank=True, null=True)
    lon = models.FloatField(verbose_name='Longitude', blank=True, null=True)
    
    def __str__(self):
        return self.mac_address
