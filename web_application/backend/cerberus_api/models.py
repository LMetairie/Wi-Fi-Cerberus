from django.db import models
from datetime import datetime


# Données colectées
class DetectedDevices(models.Model):
    # Date de collection
    date = models.DateTimeField(default= datetime.now, blank=False, verbose_name='Date de la capture')
    mac_address = models.TextField(max_length=20, unique=False, blank=False, verbose_name='Adresse MAC')
    signal_strength = models.IntegerField(blank=True, verbose_name='Puissance du signal')

    def __str__(self):
        return self.mac_address
