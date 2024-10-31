from django.db import models

class food(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="assets")
    active = models.BooleanField(default=True)
    qty = models.IntegerField(default=1)
    datecreated = models.DateTimeField(auto_now_add=True)