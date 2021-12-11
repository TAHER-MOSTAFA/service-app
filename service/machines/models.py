from django.db import models
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField
from .managers import MachineManager


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    website = models.URLField()
    image = models.ImageField()
    description = HTMLField()

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return self.name


class Machine(TimeStampedModel):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField()
    description = HTMLField()

    objects = MachineManager()

    def __str__(self) -> str:
        return self.name


class Specs(models.Model):
    label = models.CharField(max_length=10)
    value = models.CharField(max_length=50)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.label} : {self.vaue}"
