from django.db import models


class MachineManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related("company",)
        qs.prefetch_related("specs_set")
        return qs
