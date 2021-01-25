from django.db import models

from setup.models import Brand, KeyFeatures

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254, blank=False)
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'setup.Brand', related_name="brands",
        null=True, blank=False, on_delete=models.SET_NULL)
    key_feature = models.ForeignKey(
        'setup.KeyFeatures', related_name="key_features",
        null=True, blank=False, on_delete=models.SET_NULL)
    chipset_logo = models.ForeignKey(
        'setup.Brand', related_name='chipset_logos',
        null=True, blank=True, on_delete=models.SET_NULL)
    additional_logo = models.ForeignKey(
        'setup.Brand', related_name='additional_logos',
        null=True, blank=True, on_delete=models.SET_NULL)
    details = models.TextField(blank=True)
    specifications = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    has_side_banner = models.BooleanField(default=False, null=True, blank=True)
    promo_side_banner_left = models.ImageField(null=True, blank=True)
    promo_side_banner_right = models.ImageField(null=True, blank=True)
    promo_side_banner_bottom = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

