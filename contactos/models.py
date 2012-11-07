from django.db import models

# Create your models here.

from django.utils.timezone import now
class Contact(models.Model):
    name = models.CharField(max_length=200)
    lastname1 = models.CharField(max_length=200)
    lastname2 = models.CharField(max_length=200)
    age = models.IntegerField()
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('contactos_contact_detail', (), {'pk': self.pk})
