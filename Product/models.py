from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=3000)
    price = models.FloatField(default=0.0, null=False, blank=False)
    seller = models.ForeignKey(to='User.User',
                               related_name='rel_products',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ['price']
        unique_together = ['name', 'seller']

    def __str__(self):
        return self.name
