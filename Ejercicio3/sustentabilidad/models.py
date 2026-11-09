# sustentabilidad/models.py
from django.db import models

class RegistroConsumo(models.Model):
    planta = models.CharField(max_length=100)
    consumo_kwh = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.planta} - {self.consumo_kwh} kWh"