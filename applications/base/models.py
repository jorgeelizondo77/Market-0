from django.db import models


class ClaseModelo(models.Model):
    ac = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey("users.User", on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss"
    )
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True