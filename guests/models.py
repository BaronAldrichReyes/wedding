from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    is_attending = models.BooleanField(default=False, verbose_name="Attending?")
    number_of_guests = models.IntegerField(default=1, verbose_name="Total in Party")
    dietary_restrictions = models.TextField(blank=True, null=True)
    table_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    