from operator import mod
from django.db import models
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField
from .managers import MachineManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=40, unique=True)
    address = models.TextField()
    website = models.URLField()
    image = models.ImageField()
    description = HTMLField()

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return self.name

class Category(TimeStampedModel):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self) -> str:
        return self.name

class Machine(TimeStampedModel):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    cover = models.ImageField()
    description = HTMLField()
    rate = models.SmallIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])

    objects = MachineManager()

    def __str__(self) -> str:
        return self.name


class Specs(models.Model):
    label = models.CharField(max_length=10)
    value = models.CharField(max_length=50)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.label} : {self.value}"



class WishList(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machines = models.ManyToManyField(Machine)

    class Meta:
        verbose_name = ("WishList")
        verbose_name_plural = ("WishLists")

    def __str__(self):
        return str(f"{self.user.name} wish list")


class Conatact(TimeStampedModel):
    name = models.CharField(max_length=90)
    company = models.CharField(max_length=90, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_num = models.CharField(max_length=11)
    message = models.TextField()